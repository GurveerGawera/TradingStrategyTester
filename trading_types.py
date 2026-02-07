from dataclasses import dataclass
from typing import List
from enum import Enum

@dataclass
class PeriodData:
    min: int
    max: int
    open: int
    close: int
    date: str

@dataclass
class TradingData:
    data: List[PeriodData]

class Operation(Enum):
    BUY = 0,
    SELL = 1,
    HOLD = 2,
