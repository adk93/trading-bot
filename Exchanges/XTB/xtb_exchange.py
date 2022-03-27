# Standard library imports
import os
import datetime
from typing import List, Tuple
import logging

# Third party imports
import dotenv

# Local application imports
from xtb_api.xtb_api import XTBClient
from Exchanges import ExchangeConnectionError, Exchange

dotenv.load_dotenv("../.env")

USER_ID = os.environ.get("XTB_USER_ID")
PASSWORD = os.environ.get("XTB_PASSWORD")


CLIENT = XTBClient(USER_ID, PASSWORD)


class XTBDataNotFoundError(Exception):
    """Custom Error when XTB did not return expected values of market data"""
    def __init__(self, symbol):
        self.symbol = symbol

    def __str__(self):
        msg = f"XTBExchange could not retrieve data for {self.symbol}"
        logging.exception(msg)
        return msg


class XTBExchange(Exchange):
    def __init__(self):
        self.connected = False
        self.client = CLIENT

    def connect(self) -> None:
        logging.info("Connecting to XTB Exchange")
        self.client.login()
        self.connected = True

    def check_connection(self) -> None:
        if not self.connected:
            raise ExchangeConnectionError()

    def get_market_data(self, symbol: str) -> Tuple[List[float], List[datetime]]:
        self.check_connection()
        data = self.client.make_call("getChartLastRequest",
                                     {"info": {"period": 5,
                                               "symbol": symbol,
                                               "start": 1646995035000}})

        rate_info = data.get('returnData', {}).get('rateInfos', [])

        if not rate_info:
            raise XTBDataNotFoundError(symbol)

        prices = [x['open'] + x['close'] for x in rate_info]
        dates = [datetime.datetime.fromtimestamp(x['ctm'] / 1000) for x in rate_info]

        return prices, dates

    def buy(self, symbol: str):
        pass

    def sell(self, symbol: str):
        pass
