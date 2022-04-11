# Standard library imports
from abc import abstractmethod
from typing import List, Tuple
import datetime
import logging


class ExchangeConnectionError(Exception):
    """"Custom error that is raised when an exchange is not connected"""
    def __init__(self):
        logging.exception("Application could not connect to exchange")


class Exchange:

    @abstractmethod
    def get_market_data(self, symbol: str) -> Tuple[List[float], List[datetime.datetime]]:
        pass

    @abstractmethod
    def buy(self, symbol: str):
        pass

    @abstractmethod
    def sell(self, symbol: str):
        pass
