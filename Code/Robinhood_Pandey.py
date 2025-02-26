#!/usr/bin/env python

from subprocess import run
import pprint as p
import yfinance as yf
import sys
import numpy as np
import pandas as pd
from collections import OrderedDict


def bash(command):
    run(command.split())


if __name__ == "__main__":
    # print(pd.__version__)
    # print(np.__version__)
    # print(yf.__version__)

    # print("Test")
    # bash("which python")
    # for path in sys.path:
    #     print(path)
    # print(f"**** Help:\n{help(print)}")
    # print(f"**** dir:\n{dir(print)}")
    # print(f"**** doc:\n{print.__doc__}")
    ticker_symbol = "AAPL"

    # # Create a Ticker object
    ticker = yf.Ticker(ticker_symbol)

    # # Fetch historical market data
    historical_data = ticker.history(period="1mo")  # data for the last year
    print("Historical Data:")
    print(historical_data)

    # # Fetch basic financials
    financials = ticker.financials
    print("\nFinancials:")
    print(financials)

    # # Fetch stock actions like dividends and splits
    actions = ticker.actions
    print("\nStock Actions:")
    print(actions)

    # Define the ticker symbol
    ticker_symbol = "MSFT"

    # Create a Ticker object
    ticker = yf.Ticker(ticker_symbol)

    # Fetch historical market data for the last 30 days
    historical_data = ticker.history(period="1mo")  # data for the last month

    # Display a summary of the fetched data
    print(f"Summary of Historical Data for {ticker_symbol}:")
    print(historical_data[["Open", "High", "Low", "Close", "Volume"]])

    print(yf.Ticker(ticker_symbol).info["regularMarketPrice"])
    sorted_data = OrderedDict(sorted(yf.Ticker(ticker_symbol).info.items()))
    # p.pp(yf.Ticker(ticker_symbol).info, sort_dicts=False)
    p.pp(sorted_data)

    # initialise with a df with the columns
    # df = pd.DataFrame(columns=['Stock','Beta','Marketcap'])

    # here, symbol_sgx is the list of symbols (tickers) you would like to retrieve data of

    # for instance, to retrieve information for DBS, UOB, and Singtel, use the following:
    # symbol_sgx = ['D05.SI', 'U11.SI','Z74.SI']

    # for stock in symbol_sgx:
    #     ticker = yf.Ticker(stock)
    #     info = ticker.info
    #     beta = info.get('beta')
    #     marketcap = info.get('marketCap')
    #     df_temp = pd.DataFrame({'Stock':stock,'Beta':[beta],'Marketcap':[marketcap]})
    #     df = pd.concat([df, df_temp], ignore_index=True)

    # this line allows you to check that you retrieved the right information
    # df

    # Aim is to do the following:
    #
