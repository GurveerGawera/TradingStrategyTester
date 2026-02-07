from trading_types import PeriodData
from strategies import TradingStrategy
from typing import List

def trading_loop(trading_data: List[PeriodData], trading_strategy: TradingStrategy) -> List[float]:
    balance : List[float] = []
    for index, _ in enumerate(trading_data):
        trading_strategy.strategy(trading_data[0:index])
        balance.append(trading_strategy.balance(trading_data[index].close))
    trading_strategy.sell_all(trading_data[-1].close)
    return balance