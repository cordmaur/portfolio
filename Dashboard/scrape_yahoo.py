# from datetime import datetime
# import numpy as np
from datetime import datetime

import numpy as np
import pandas as pd

from dashboards.yahoo_parser import YahooParser


print("Getting the current portfolio")
columns = {
    "ATIVO": "Ticker",
    "PREÇO MÉDIO": "AvgPrice",
    "PREÇO ATUAL": "Price",
    "QUANTIDADE": "Qty",
}
portfolio = pd.read_csv(
    "./Dashboard/CarteiraStatusInvest.csv", encoding="utf-8", sep=";", decimal=","
)[columns.keys()]
portfolio = portfolio.rename(columns=columns)
portfolio["Qty"] = portfolio["Qty"].astype("int")
portfolio["AvgPrice"] = portfolio["AvgPrice"].round(2)

print(len(portfolio))

print("Creating YahooParser instance")
yahoo = YahooParser(headless=True)

# print("Retrieving values for one ticker")
# results = yahoo.get_ticker_values("ITSA4")
# print(results)


print("Scraping tickers")
alternate_tickers = {
    "ITSA3": {"ticker": "ITSA4"},
    "SANB3": {"ticker": "SANB11", "factor": 0.5},
}
results = yahoo.get_tickers(portfolio["Ticker"], alternate_tickers=alternate_tickers)

portfolio = pd.concat([portfolio.set_index("Ticker"), results], axis=1)
portfolio["Price"] = portfolio["quote"]
portfolio = portfolio.drop(columns="quote")
portfolio["Volume"] = portfolio["Qty"] * portfolio["Price"]

portfolio["analists"] = portfolio["analists"].replace("", 0).fillna(0).astype("int")

portfolio = portfolio.replace("", np.nan)
portfolio["Date"] = datetime.now().strftime("%Y-%m-%d")
portfolio["Upside"] = (portfolio["mean"] / portfolio["Price"]) - 1

portfolio["Upside"] = ((100 * portfolio["Upside"]).round(1)).astype("str") + "%"

portfolio.reset_index().rename(columns={"index": "Stock"}).to_json(
    f'./Dashboard/data/portfolio_{datetime.now().strftime("%Y%m%d")}.json',
    orient="records",
)
