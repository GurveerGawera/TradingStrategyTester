from trading_types import PeriodData
from typing import List

class TradingStrategy:
    def __init__(self, money: float):
        self.money: float = money # money in dollars
        self.shares: float = 0.000

    def sell_all(self, share_price: float):
        self.money += self.shares * share_price
        self.shares = 0

    def balance(self, share_price: float) -> float:
        return self.money + (share_price * self.shares)

    def strategy(self):
        raise NotImplementedError("strategy function not implemented!")

class BuyAndHold(TradingStrategy):
    def __init__(self, money: float):
        super().__init__(money)

    def strategy(self, data: List[PeriodData]):
        """
        Execute Buy and Hold Strategy
        
        :param trading_history: history of trading data 
        :return: Tuple containing operation and the amount of money we want to use with the operation.
        """
        if (len(data) == 1): 
            # look to buy all we can
            self.shares = self.money / data[0].close
            self.money = 0
            return 
        return