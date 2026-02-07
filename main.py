import yfinance as yf
import mplfinance as mpf
import numpy as np
from trading_loop import trading_loop
from trading_types import PeriodData
from strategies import BuyAndHold

# Function to get historic data and return in a pandas dataframe
def get_trading_data(period='1y'):
    data=yf.Ticker('^GSPC').history(period=period)
    data['Balance'] = 0
    return data

# Plot the data in trades as a candlestick diagram
def plot_data(trades, balances):
    extra_plot = mpf.make_addplot(trades['Balance'], color='#606060', panel=2, ylabel='balances', secondary_y=False)
    mpf.plot(trades, volume=True, type='candle', tight_layout=True, style='yahoo', addplot=extra_plot)


# take the historic trade data and wisely invest the initial_investment
# returns a list (or amended dataframe) that contains the balance for each day during the trading period
def execute_strategies(trades, initial_investment):

    return trades

if __name__ == "__main__":
    print("Trading is fun!")

    # get historic data for S&P
    trades = get_trading_data()

    trading_data = []
    trading_strategy = BuyAndHold(money=100)

    for trade in trades.iterrows():
        trading_data.append(PeriodData(
            min=trade[1]["Low"],
            max=trade[1]["High"],
            open=trade[1]["Open"],
            close=trade[1]["Close"],
            date=trade[0]
        ))
    
    balance = trading_loop(trading_data, trading_strategy)

    print("Initial Trading Data: ", trading_data[0].close)
    print("Final Trading Data: ", trading_data[-1].close)

    print(trading_strategy.money)
    print(trading_strategy.shares)