import yfinance as yf
import pandas_ta_classic as ta

def get_trading_data():
    data=yf.Ticker('^GSPC').history(period='1y')
    print(data)
    return data

if __name__ == "__main__":
    print("Trading is fun!")
    trades = get_trading_data()