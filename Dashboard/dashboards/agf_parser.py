# This module parses the AGF site
# the main objective is to extract the tables from the portfolio

from pathlib import Path
from time import sleep

import pandas as pd

from .selenium_utils import SeleniumPage
from selenium.webdriver.common.by import By

# Other chrome options that could be used
# chrome_options.add_argument(' headless')
# chrome_options.add_argument(' —-no-sandbox')
# chrome_options.add_argument(' —-disable-dev-shm-usage')

# chrome_options.add_argument('--disable-dev-shm-usage')
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--start-maximized')
# chrome_options.add_argument('--start-fullscreen')
# chrome_options.add_argument('--single-process')


class Portfolio:
    default_types = {
        "previdenciaria": {
            "expected_value": "Carteira Previdenciária",
            "goto_button": "//*[@id='sidebarAportador']/ul/li[3]/a",
            "as_table": "//*[@id='main']/div[2]/div[2]/span[4]/span/a[4]",
            "more_options": "//*[@id='main']/div[2]/div[2]/span[4]/button",
        },
        "oportunidade": {
            "expected_value": "Carteira Oportunidades",
            "goto_button": "//*[@id='sidebarAportador']/ul/li[4]/a",
            "as_table": "//*[@id='main']/div[2]/div[2]/span[3]/span/a[3]",
            "more_options": "//*[@id='main']/div[2]/div[2]/span[3]/button",
        },
    }

    elements = dict(
        header="//*[@id='main']/div[1]/div/div/h4",
        table="//*[@id='carteira-visao-tabela']",
        dy_type="//*[@id='main']/div[2]/div[2]/span[1]/a",
    )

    dy_types = ["medio", "projetivo"]

    @property
    def portfolio_values(self):
        return self.default_types[self.portfolio_type]

    @property
    def goto_button(self):
        return Portfolio.default_types[self.portfolio_type]["goto_button"]

    @property
    def expected_value(self):
        return Portfolio.default_types[self.portfolio_type]["expected_value"]

    def __init__(self, page: SeleniumPage, portfolio_type: str) -> None:
        if portfolio_type not in Portfolio.default_types.keys():
            raise Exception(
                f"Carteira {portfolio_type} not available. Choose between: {Portfolio.default_types.keys()}"
            )

        self.portfolio_type = portfolio_type
        self.page = page

    def in_portfolio(self) -> bool:

        # Check if header exists and if we are inside the correct portfolio
        return self.page.element_exists(Portfolio.elements["header"]) and (
            self.page.get_value(Portfolio.elements["header"]) == self.expected_value
        )

    def go_to_portfolio(self):

        # if not in the desired portfolio, go to it and wait for loading
        if not self.in_portfolio():
            print(f"Carregando {self.expected_value}")
            self.page.click(self.goto_button)
            self.page.wait_for_value(
                Portfolio.elements["header"], self.expected_value, post_wait=0.1
            )

        else:
            print(f"Ja estava na {self.expected_value}")

        # once in the desired page, dismiss possible alerts
        self.page.dismiss_alerts()

        # check table view. Click on more_options if it is not loaded correctly
        if (
            not self.page.element_exists(self.portfolio_values["as_table"])
            or self.page.get_value(self.portfolio_values["as_table"]) == ""
        ):
            self.page.click(self.portfolio_values["more_options"])

        # if in cards view, switch to table view
        if self.page.get_value(self.portfolio_values["as_table"]) == "Visão Tabela":
            self.page.click(self.portfolio_values["as_table"])

            # and wait for the table to load completely
            print("Aguardando mudar para tabela")
            self.page.wait_for_element(Portfolio.elements["table"], post_wait=0.2)
        else:
            print("Já está como tabela")

    def change_dy_type(self, dy_type: str):

        # First, let's make sure we are in the previdenciaria by checking the button
        if not self.page.element_exists(Portfolio.elements["dy_type"]):
            raise Exception("Não está na carteira previdenciaria")

        if dy_type not in Portfolio.dy_types:
            raise Exception(
                f"DPA {dy_type} não suportado. Deve ser {Portfolio.dy_types}"
            )

        dy_value = self.page.get_value(Portfolio.elements["dy_type"])

        if (dy_type == "projetivo" and dy_value == "Ver com DPA Projetivo") or (
            dy_type == "medio" and dy_value == "Ver com DPA Médio"
        ):
            print(f"Mudando para DPA {dy_type}")
            self.page.click(Portfolio.elements["dy_type"])

            # now, wait for the alert to dismiss
            self.page.dismiss_alerts(wait_for_alert=True)
            sleep(0.2)

        else:
            print(f"DPA {dy_type} já configurado")


class AgfParser:
    agf_url = "https://www.agfmais.com.br"

    elements = {
        "login": "//*[@id='loginform-username']",
        "pwd": "//*[@id='loginform-password']",
        "enter": "//*[@id='login-form']/div[4]/button",
        "header": "//*[@id='w1']/div[2]/table",
        "table": "//*[@id='carteira-visao-tabela']",
    }

    def __init__(self, login: str, password: str, headless: bool = True, **kwargs):
        self.login, self.password = login, password

        # open the corresponding page
        self.page = SeleniumPage(AgfParser.agf_url, headless=headless, **kwargs)

    def signin(self):
        self.page.fill_input(element=AgfParser.elements["login"], value=self.login)
        self.page.fill_input(element=AgfParser.elements["pwd"], value=self.password)

        self.page.click(element=AgfParser.elements["enter"])

    def inside_portfolio(self, portfolio: str):
        """
        Check if current page corresponds to the portfolio

        Args:
            portfolio (str): ['precidenciaria', 'oportunidade']
        """

        return Portfolio(self.page, portfolio).in_portfolio()

    def open_oportunidades(self):
        portfolio = Portfolio(self.page, "oportunidade")
        portfolio.go_to_portfolio()

        pass

    def open_previdenciaria(self, dy_type: str = "mean"):

        portfolio = Portfolio(self.page, "previdenciaria")
        portfolio.go_to_portfolio()

        portfolio.change_dy_type(dy_type)

    def get_df(self):

        # first we will get the header
        header_el = self.page.driver.find_element(
            By.XPATH, value=AgfParser.elements["header"]
        )
        header_html = header_el.get_attribute("outerHTML")
        header_df = pd.read_html(header_html)[0]

        table_el = self.page.driver.find_element(
            By.XPATH, value=AgfParser.elements["table"]
        )
        table_html = table_el.get_attribute("outerHTML")

        table_df = pd.read_html(table_html, decimal=",", thousands=".")[0]
        table_df.columns = header_df.columns

        # correct percentage symbol
        columns = ["YoC"]
        if "DYProjetivo" in table_df.columns:
            columns = columns + ["DYProjetivo"]
        else:
            columns = columns + ["DYMédio"]

        for column in columns:
            if column in table_df.columns:
                table_df[column] = (
                    table_df[column].str.replace("%", "").str.replace(",", ".")
                )

        # correct currency symbol
        for column in [
            "PreçoTeto",
            "Cotação",
            "Preço Médio",
            "PreçoMédioAjustado",
            "Preço Médio Ajustado",
        ]:
            if column in table_df.columns:
                table_df[column] = (
                    table_df[column]
                    .str.replace("R$ ", "", regex=False)
                    .str.replace(",", ".")
                )

        return table_df

    def export_dfs(self, folder: str = "data/"):
        """
        Export the dataframes to a specific folder.

        Args:
            folder (str, optional): output folder. Defaults to 'data/'.
        """

        # First get the Oportunidades
        portfolio = Portfolio(self.page, "oportunidade")
        portfolio.go_to_portfolio()
        target = Path(folder) / f"oportunidade_raw.pickle"
        self.get_df().to_pickle(target)

        # Then get the Precidenciaria
        portfolio = Portfolio(self.page, "previdenciaria")

        for dy_type in Portfolio.dy_types:
            target = Path(folder) / f"{dy_type}_raw.pickle"
            self.open_previdenciaria(dy_type=dy_type)
            df = self.get_df()
            df.to_pickle(target)

    def close(self):
        self.page.driver.quit()
