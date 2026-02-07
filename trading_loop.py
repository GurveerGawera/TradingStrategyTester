from trading_types import PeriodData
from strategies import TradingStrategy
from typing import List

def trading_loop(trading_data: List[PeriodData], strategy: TradingStrategy):
    for index, period in enumerate(trading_data):
        strategy.strategy(trading_data[0:index])
    strategy.sell_all(trading_data[-1].close)
    return