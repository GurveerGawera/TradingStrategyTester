import yfinance as yf
import mplfinance as mpf
from trading_loop import trading_loop
from trading_types import PeriodData
from strategies import BuyAndHold, TradingStrategy
from typing import List

# Function to get historic data and return in a pandas dataframe
def get_trading_data(period='1y'):
    data=yf.Ticker('^GSPC').history(period=period)
    data['Balance'] = 0
    return data

# Plot the data in trades as a candlestick diagram
def plot_data(trades, all_strategies: List[TradingStrategy]):
    for strategy in all_strategies:
        extra_plot = mpf.make_addplot(trades[str(strategy)], color='#606060', panel=2, ylabel=f"{str(strategy)}_Balance", secondary_y=False)
    mpf.plot(trades, volume=True, type='candle', tight_layout=True, style='yahoo', addplot=extra_plot)

if __name__ == "__main__":
    print("Trading is fun!")

    # get historic data for S&P
    trades = get_trading_data()

    trading_data = []
    trading_strategy = BuyAndHold(money=10000)

    all_strategies : List[TradingStrategy] = [trading_strategy]

    for trade in trades.iterrows():
        trading_data.append(PeriodData(
            min=trade[1]["Low"],
            max=trade[1]["High"],
            open=trade[1]["Open"],
            close=trade[1]["Close"],
            date=trade[0]
        ))
    
    balance = trading_loop(trading_data, trading_strategy)

    trades[str(trading_strategy)] = balance

    plot_data(trades, all_strategies)