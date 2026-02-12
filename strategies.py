from trading_types import PeriodData
from typing import List
import random
import statistics

class TradingStrategy:
    def __init__(self, money: float):
        self.money: float = money # money in dollars
        self.shares: float = 0.000
        self.balance: List[float] = []
        self.starting_money: float = money
    
    def __str__(self):
        return self.__class__.__name__ + ": $" + str(int(self.money)) + ": +/-" + str(int(self.money / self.starting_money)) + "%"

    def sell_all(self, share_price: float):
        self.money += self.shares * share_price
        self.shares = 0

    def add_balance(self, share_price: float) -> float:
        self.balance.append(self.money + (share_price * self.shares))
        return

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

class CoinToss(TradingStrategy):
    def __init__(self, money: float):
        super().__init__(money)

    def strategy(self, data: List[PeriodData]):
        """
        Execute a coin toss. If heads, then buy (if not already bought). If tails, sell (if not already sold)

        :param trading_history: history of trading data
        :return: Tuple containing operation and the amount of money we want to use with the operation.
        """
        if len(data)==0: return
        if random.randint(0,1)==0:
            #buy
            if self.money>0:
                self.shares = self.money / data[-1].close
                self.money = 0
        else:
            #sell
            if self.shares>0:
                self.money += self.shares * data[-1].close
                self.shares = 0

        return
    
class SMA(TradingStrategy):
    def __init__(self, money, short_sma, long_sma):
        super().__init__(money)
        self.short_sma = short_sma
        self.long_sma = long_sma
        self.prev_short_avg = 0
        self.prev_long_avg = 0

    def strategy(self, data: List[PeriodData]):
        # TODO: Next steps would probably be to plot the short_sma and long_sma alongside the Balance. 
        if len(data) < self.long_sma: return
        # Extract the most recent closing prices, where len(close_prices) == self.long_sma
        close_prices = [d.close for d in data[-self.long_sma:]]
        cur_short_avg = statistics.fmean(close_prices[-self.short_sma:])
        cur_long_avg = statistics.fmean(close_prices)

        if self.prev_short_avg == 0 or self.prev_long_avg == 0:
            self.prev_short_avg = cur_short_avg
            self.prev_long_avg = cur_long_avg
            return
        
        if self.prev_short_avg > self.prev_long_avg and cur_short_avg < cur_long_avg and self.shares != 0:
            self.money = self.shares * data[-1].close
            self.shares = 0
        elif self.prev_short_avg < self.prev_long_avg and cur_short_avg > cur_long_avg and self.money != 0:
            self.shares = self.money / data[-1].close
            self.money = 0

        self.prev_short_avg = cur_short_avg
        self.prev_long_avg = cur_long_avg