from .types import State, Operation
from typing import Tuple
from dataclasses import dataclass
# buy and hold, only sell at end
# buy and sell depending on moving average

# input?
#

class TradingStrategy:
    def strategy(self):
        raise NotImplementedError("strategy function not implemented!")
    

class BuyAndHold(TradingStrategy):
    def strategy(trading_history: State) -> Tuple[Operation, int]:
        """
        Docstring for buy_and_hold
        
        :param trading_history: history of trading data 
        :return: Tuple containing operation and the amount of money we want to use with the operation.
        """
        if (len(trading_history.data) == 1): 
            return 1 
        return 1