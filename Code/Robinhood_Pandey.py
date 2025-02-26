#!/usr/bin/env python

import yfinance as yf
from subprocess import run
import sys


def bash(command):
    run(command.split())


if __name__ == "__main__":
    # print("Test")
    # bash("which python")
    # for path in sys.path:
    #     print(path)
    # print(f"**** Help:\n{help(print)}")
    # print(f"**** dir:\n{dir(print)}")
    # print(f"**** doc:\n{print.__doc__}")
    # ticker_symbol = "AAPL"

    # # Create a Ticker object
    # ticker = yf.Ticker(ticker_symbol)

    # # Fetch historical market data
    # historical_data = ticker.history(period="1m")  # data for the last year
    # print("Historical Data:")
    # print(historical_data)

    # # Fetch basic financials
    # financials = ticker.financials
    # print("\nFinancials:")
    # print(financials)

    # # Fetch stock actions like dividends and splits
    # actions = ticker.actions
    # print("\nStock Actions:")
    # print(actions)

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
