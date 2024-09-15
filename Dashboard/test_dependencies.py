# from datetime import datetime
# import numpy as np
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
portfolio["Volume"] = portfolio["Qty"] * portfolio["Price"]
portfolio["AvgPrice"] = portfolio["AvgPrice"].round(2)

print(len(portfolio))

print("Creating YahooParser instance")
yahoo = YahooParser(headless=True)

alternate_tickers = {
    "ITSA3": {"ticker": "ITSA4"},
    "SANB3": {"ticker": "SANB11", "factor": 0.5},
}

# results = yahoo.get_tickers(portfolio['Ticker'], alternate_tickers=alternate_tickers)

print("Retrieving values for one ticker")
results = yahoo.get_ticker_values("ITSA4")
print(results)
