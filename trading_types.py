from dataclasses import dataclass
from typing import List
from enum import Enum

@dataclass
class PeriodData:
    min: float
    max: float
    open: float
    close: float
    date: str

class Operation(Enum):
    BUY = 0,
    SELL = 1,
    HOLD = 2,
