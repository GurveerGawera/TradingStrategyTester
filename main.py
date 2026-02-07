import yfinance as yf
import mplfinance as mpf
from trading_loop import trading_loop
from trading_types import PeriodData
from strategies import BuyAndHold, TradingStrategy, CoinToss
from typing import List
from matplotlib.ticker import MultipleLocator

# Function to get historic data and return in a pandas dataframe
def get_trading_data(period='2y'):
    data=yf.Ticker('^GSPC').history(period=period)
    return data

# Plot the data in trades as a candlestick diagram
def plot_data(trades, all_strategies: List[TradingStrategy]):
    extra_plots=[]
    for strategy in all_strategies:
        extra_plots.append(mpf.make_addplot(trades[str(strategy)], panel=1, label=str(strategy), secondary_y=False))
    fig, axlist = mpf.plot(trades, type='candle', tight_layout=True, style='yahoo', addplot=extra_plots, ylabel="Price", returnfig=True)
    axlist[0].xaxis.set_minor_locator(MultipleLocator(1))
    axlist[0].xaxis.set_major_locator(MultipleLocator(7))
    mpf.show()

if __name__ == "__main__":
    print("Trading is fun!")

    # get historic data for S&P
    trades = get_trading_data()

    trading_data = []
    initial=10000
    trading_strategy = BuyAndHold(money=initial)
    rand_strat = CoinToss(money=initial)

    all_strategies : List[TradingStrategy] = [trading_strategy, rand_strat]

    for trade in trades.iterrows():
        trading_data.append(PeriodData(
            min=trade[1]["Low"],
            max=trade[1]["High"],
            open=trade[1]["Open"],
            close=trade[1]["Close"],
            date=trade[0]
        ))
    
    trading_loop(trading_data, all_strategies)

    for strat in all_strategies:
        trades[str(strat)] = strat.balance

    plot_data(trades, all_strategies)