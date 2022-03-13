# Standard library imports
from typing import List
import datetime

# Third-party imports
import numpy as np

# Local app imports
from .strategies import Strategy

class Trader:
    """Trader module makes calculation and makes decisions to buy or not to buy"""
    def __init__(self, ticker: str, prices: List[float], dates: List[datetime.datetime]):
        self.ticker = ticker
        self.prices = prices
        self.dates = dates
        self.strategies = list()

    @classmethod
    def from_xtbapi(cls, ticker: str, rate_info_records: List):
        """Takes as a parameter a list of XTB rate info records"""
        prices = [x['open'] + x['close'] for x in rate_info_records]
        dates = [datetime.datetime.fromtimestamp(x['ctm']/1000) for x in rate_info_records]

        return cls(ticker, prices, dates)

    def add_strategies(self, *strategies: List[Strategy]):
        for strategy in strategies:
            self.strategies.append(strategy)

    @property
    def read_strategies(self):
        return [str(x) for x in self.strategies]

    def get_decisions(self):
        for strategy in self.strategies:
            s = strategy(self.prices, self.dates)
            d = s.decision()
            print(f"{s} suggests {d}")



