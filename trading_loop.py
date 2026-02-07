from trading_types import PeriodData
from strategies import TradingStrategy
from typing import List

def trading_loop(trading_data: List[PeriodData], trading_strategies: List[TradingStrategy]) -> List[float]:
    for index, _ in enumerate(trading_data):
        for strat in trading_strategies:
            strat.strategy(trading_data[0:index])
            strat.add_balance(trading_data[index].close)
    for strat in trading_strategies:
        strat.sell_all(trading_data[-1].close)
    return