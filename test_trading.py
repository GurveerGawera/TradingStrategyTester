import sys
import os

sys.path.append(os.path.dirname(__file__))  # add current folder to path

from trading_types import PeriodData
from trading_loop import trading_loop
from strategies import BuyAndHold

def test_trading():
    day1 = PeriodData(min=0, max=10, open=0, close=5, date=1)
    day2 = PeriodData(min=5, max=15, open=5, close=10, date=2)
    day3 = PeriodData(min=10, max=20, open=10, close=15, date=3)

    trading_strategy = BuyAndHold(100.00)

    trading_loop([day1, day2, day3], trading_strategy)

    # buy at 5, 100/5 = 20 shares
    # sell 20 shares at end, price: 15. 20 * 15 = 300
    assert trading_strategy.money == 300.00
    assert trading_strategy.shares == 0.00




