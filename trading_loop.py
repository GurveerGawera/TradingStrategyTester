from .types import TradingData
from strategies import TradingStrategy

def trading_loop(all_data: TradingData, strategy: TradingStrategy):
    for period in all_data:
        print(period)
    return