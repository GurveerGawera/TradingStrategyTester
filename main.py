import yfinance as yf
import pandas_ta_classic as ta
from trading_loop import trading_loop
import mplfinance as mpf
import numpy as np

# Function to get historic data and return in a pandas dataframe
def get_trading_data(period='1y'):
    data=yf.Ticker('^GSPC').history(period=period)
    return data

# Plot the data in trades as a candlestick diagram
def plot_data(trades, balances):
    extra_plot = mpf.make_addplot(trades['balance'], color='#606060', panel=2, ylabel='balances', secondary_y=False)
    mpf.plot(trades, volume=True, type='candle', tight_layout=True, style='yahoo', addplot=extra_plot)


# take the historic trade data and wisely invest the initial_investment
# returns a list (or amended dataframe) that contains the balance for each day during the trading period
def execute_strategies(trades, initial_investment):
    trades['balance'] = np.random.default_rng().integers(1, 1000, len(trades))
    return trades

if __name__ == "__main__":
    print("Trading is fun!")

    # get historic data for S&P
    trades = get_trading_data()

    initial_investment = 1000

    balances = execute_strategies(trades,initial_investment)

    plot_data(trades, balances)