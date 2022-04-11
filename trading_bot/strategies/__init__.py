from abc import abstractmethod
from typing import List
import datetime
from collections import namedtuple

import numpy as np


class Strategy:
    def __init__(self, prices: List[float], dates: List[datetime.datetime]):
        self.prices = np.array(prices)
        self.dates = np.array(dates)

    @abstractmethod
    def should_buy(self) -> bool:
        pass

    @abstractmethod
    def should_sell(self) -> bool:
        pass

    @abstractmethod
    def backtesting(self) -> List[namedtuple]:
        pass

    @abstractmethod
    def calibrate(self) -> List[namedtuple]:
        pass