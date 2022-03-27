from abc import abstractmethod
from typing import List

import numpy as np


class Strategy:
    def __init__(self, prices: List[float], dates):
        self.prices = np.array(prices)
        self.dates = np.array(dates)

    @abstractmethod
    def should_buy(self) -> bool:
        pass

    @abstractmethod
    def should_sell(self) -> bool:
        pass