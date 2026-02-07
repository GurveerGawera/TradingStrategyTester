import yfinance as yf
import pandas_ta_classic as ta
from trading_loop import trading_loop
import mplfinance as mpf

# Function to get historic data and return in a pandas dataframe
def get_trading_data(period='1y'):
    data=yf.Ticker('^GSPC').history(period=period)
    return data

# Plot the data in trades as a candlestick diagram
def plot_data(trades):
    mpf.plot(trades, volume=True, type='candle', mav=20, tight_layout=True, style='yahoo')

# take the historic trade data and wisely invest the initial_investment
# returns a list (or amended dataframe) that contains the balance for each day during the trading period
def execute_strategies(trades, initial_investment):
    pass

if __name__ == "__main__":
    print("Trading is fun!")

    # get historic data for S&P
    trades = get_trading_data()

    initial_investment = 1000

    balances = execute_strategies(trades,initial_investment)

    plot_data(trades, balances)