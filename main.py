import yfinance as yf
import pandas_ta_classic as ta
from trading_loop import trading_loop
import mplfinance as mpf

def get_trading_data():
    data=yf.Ticker('^GSPC').history(period='1y')
    print(data)
    return data

def plot_data(trades):
    mpf.plot(trades, volume=True, type='candle', mav=20, tight_layout=True, style='yahoo')



if __name__ == "__main__":
    print("Trading is fun!")
    trades = get_trading_data()
    print(trades.info())
    plot_data(trades)