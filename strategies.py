from trading_types import PeriodData, Operation
from typing import Tuple, List

class TradingStrategy:
    def __init__(self, money: int):
        self.money = money
        self.shares = 0
    def strategy(self):
        raise NotImplementedError("strategy function not implemented!")

class BuyAndHold(TradingStrategy):
    def __init__(self, money: int):
        super.__init__(money)

    def strategy(self, data: List[PeriodData]) -> Tuple[Operation, int]:
        """
        Execute Buy and Hold Strategy
        
        :param trading_history: history of trading data 
        :return: Tuple containing operation and the amount of money we want to use with the operation.
        """
        if (len(data) == 1): 
            return (Operation.BUY, self.money)
        return (Operation.HOLD, 0)