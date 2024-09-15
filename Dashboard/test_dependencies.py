from selenium import webdriver

try:
    from dashboards.selenium_utils import SeleniumPage
    from dashboards.yahoo_parser import YahooParser

    print("Imports OK")
except Exception as e:
    print(e)
