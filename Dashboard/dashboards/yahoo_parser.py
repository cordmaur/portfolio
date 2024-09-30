"""dashboards.yahoo_parser

This module contains a class YahooParser to parse the recomendations from Yahoo Finance.

"""
from datetime import datetime
import pandas as pd

from ast import literal_eval

from .selenium_utils import SeleniumPage


class YahooParser:
    """
    A class to parse the recomendations from Yahoo Finance.

    Attributes
    ----------
    url : str
        The Yahoo Finance url.
    elements : dict
        A dict with the selectors for each element.
    results : list
        The list of elements to be parsed.
    page : SeleniumPage
        The selenium page object.
    df : pandas.DataFrame
        The dataframe containing the parsed data.
    """

    url = "https://br.financas.yahoo.com/quote/"

    # Yahoo Finance elements
    elements = dict(
        quote='//*[@id="Col2-10-QuoteModule-Proxy"]/div/section/div/div[1]/div[3]/div[3]/span[2]',
        recomendation='//*[@id="Col2-9-QuoteModule-Proxy"]/div/section/div/div/div[1]',
        low='//*[@id="Col2-10-QuoteModule-Proxy"]/div/section/div/div[2]/div[1]/span[2]',
        mean='//*[@id="Col2-10-QuoteModule-Proxy"]/div/section/div/div[1]/div[4]/div[1]/span[2]',
        high='//*[@id="Col2-10-QuoteModule-Proxy"]/div/section/div/div[2]/div[2]/span[2]',
        analists='//*[@id="Col2-10-QuoteModule-Proxy"]/div/section/a/h2',
    )

    results = ["quote", "recomendation", "low", "mean", "high", "analists"]

    def __init__(self, headless: bool = True) -> None:

        # Open the Yahoo Finance pages and click the agree button
        self.page = SeleniumPage(url=None, headless=headless)
        self.df = None

    def get_ticker_values(self, ticker: str) -> dict:
        """
        Retrieves the values for a given ticker symbol from Yahoo Finance.

        Parameters:
        ticker (str): The ticker symbol to retrieve values for.

        Returns:
        dict: A dictionary containing the retrieved values, including quote,
        recomendation, low, mean, high, and analists.
        """
        # Check if the ticker is in the right format
        if ticker.split(".")[-1] != "SA":
            ticker = ticker + ".SA"

        # open the ticker quotes page
        url = YahooParser.url + ticker
        self.page.get(url)

        # scroll all way down
        self.page.scroll_down(2, height=1000, sleep_time=1.0)

        # get the results
        results = {
            result: self.page.get_value(
                YahooParser.elements[result], wait_time=1.0, dont_wait=False
            ).replace(",", ".")
            for result in YahooParser.results
        }

        # parse the analists number
        analists = results["analists"]
        analists = analists[analists.find("(") + 1 : analists.find(")")]
        results["analists"] = analists

        # Convert the values to float
        for result in YahooParser.results:
            try:
                results[result] = literal_eval(results[result])
            except Exception:  # pylint: disable=broad-except
                results[result] = ""

        return results

    def get_ticker(self, ticker: str, alternate_ticker: dict = None):
        """
        Retrieves the values for a given ticker symbol from Yahoo Finance,
        including the option to apply a factor to the results.

        Parameters:
        ticker (str): The ticker symbol to retrieve values for.
        alternate_ticker (dict): An optional dictionary containing an alternate ticker symbol
        and/or a factor to apply to the results.

        Returns:
        dict: A dictionary containing the retrieved values, including quote, low, mean, high,
        and analists, with the option to apply a factor to the results.
        """

        print(f"Fetching ticker {ticker}")
        start = datetime.now()

        if alternate_ticker is not None:
            ticker = alternate_ticker["ticker"]

        results = self.get_ticker_values(ticker=ticker)

        if alternate_ticker is not None and "factor" in alternate_ticker:
            for result in ["low", "mean", "high", "quote"]:
                results[result] = results[result] * alternate_ticker["factor"]

        delta = datetime.now() - start
        print(f'Elapsed time: {str(delta)}')
        print(results)
        return results

    def get_tickers(
        self, tickers: list, alternate_tickers: dict = None, retries: int = 3
    ):
        """
        Fetch the results for multiple tickers.

        Args:
            tickers (list): List of tickers to fetch.
            alternate_tickers (dict, optional): Dictionary with ticker as key and dict as value.
                This dict must have the keys "ticker" and "factor".
                If the ticker is in the dict, it will be used instead of the original ticker.
                The factor will be used to multiply the results.
            retries (int, optional): Number of retries if the fetch fails. Defaults to 3.

        Returns:
            pd.DataFrame: DataFrame with the results. The index is the ticker, the columns are
                the results.
        """

        results = {}

        retry = 3
        for ticker in tickers:
            # try to fetch the ticker multiple times
            retry = 0

            while retry < retries:
                try:
                    # if the ticker is in the alternate_tickers dict, use the alternate ticker
                    # and factor
                    if ticker in alternate_tickers:
                        alternate_ticker = alternate_tickers[ticker]
                    else:
                        alternate_ticker = None

                    # fetch the ticker and add it to the results
                    results[ticker] = self.get_ticker(
                        ticker=ticker, alternate_ticker=alternate_ticker
                    )

                    # print(results[ticker])
                    retry = retries

                except Exception as e:
                    # if the fetch fails, increment the retry counter
                    retry += 1
                    print(f"Error fetching {ticker}. Retries={retry}")
                    print(e)

        # return a DataFrame with the results
        return pd.DataFrame(results).T

    def export_df(self, tickers: list):

        yahoo_results = self.get_tickers(tickers)
        self.df = pd.DataFrame(yahoo_results).T
        self.df.index.name = "Empresa"
        self.df.reset_index(inplace=True)
        self.df.to_pickle("data/yahoo_raw.pickle")
