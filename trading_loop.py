from trading_types import TradingData
from strategies import TradingStrategy

def trading_loop(all_data: TradingData, strategy: TradingStrategy):
    for index, period in enumerate(all_data):
        strategy.strategy(all_data[0:index])
        print(period)
    return