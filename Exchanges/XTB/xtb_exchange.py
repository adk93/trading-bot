# Standard library imports
import os
import datetime
from typing import List, Tuple
import logging
from pathlib import Path

# Third party imports
import dotenv

# Local application imports
from xtb_api.xtb_api import XTBClient
from Exchanges import ExchangeConnectionError, Exchange


env_path = Path(__file__).resolve().parents[2]

dotenv.load_dotenv(os.path.join(env_path,'.env'))

USER_ID = os.environ.get("XTB_USER_ID")
PASSWORD = os.environ.get("XTB_PASSWORD")

CLIENT = XTBClient(USER_ID, PASSWORD)


class XTBDataNotFoundError(Exception):
    """Custom Error when XTB did not return expected values of market data"""
    def __init__(self, symbol, data):
        self.symbol = symbol
        self.data = data

    def __str__(self):
        msg = f"XTBExchange could not retrieve data for {self.symbol}"
        logging.exception(msg)
        logging.exception(self.data)
        return msg


class XTBExchange(Exchange):
    """
    Class that handles getting market data, buying and selling securities
    Class is based on xtb client

    """
    def __init__(self):
        self.connected = False
        self.client = CLIENT
        self.session_id = None

    def connect(self) -> None:
        logging.info("Connecting to XTB Exchange")
        response = self.client.login()
        if not response.get('status'):
            raise ExchangeConnectionError()
        self.connected = True
        self.session_id = response.get('streamSessionId')

    def check_connection(self) -> None:
        if not self.connected:
            raise ExchangeConnectionError()

    def get_market_data(self,
                        symbol: str,
                        start: datetime.datetime = datetime.datetime(2021, 1, 1),
                        period: int = 1440) -> Tuple[List[float], List[datetime.datetime]]:
        """
        Gets market data ie. prices and dates based on given params
        :param symbol: ticker as a string
        :param period: data interval. Default 1440 minutes. Possible arguments in the xtb documentation
        :param start: starting point in time for gathering data
        :return: Tuple comprising of prices and datetimes
        """
        self.check_connection()
        data = self.client.make_call("getChartLastRequest",
                                     {"info": {"period": period,
                                               "symbol": symbol,
                                               "start": start.timestamp() * 1000}})

        rate_info = data.get('returnData', {}).get('rateInfos', [])

        if not rate_info:
            raise XTBDataNotFoundError(symbol, data)

        prices = [x['open'] + x['close'] for x in rate_info]
        dates = [datetime.datetime.fromtimestamp(x['ctm'] / 1000) for x in rate_info]

        return prices, dates

    def buy(self, symbol: str):
        pass

    def sell(self, symbol: str):
        pass

    def get_trades(self) -> List[Tuple[str, float]]:
        """
        Returns a list of tuples comprising of stock symbol and volume (in lots)
        :return: List[Tuple[symbol, volume]]
        """
        self.check_connection()
        data = self.client.make_call("getTrades", {"openedOnly": True})

        if not data.get("status"):
            raise XTBDataNotFoundError("GET TRADES", data)

        return list(map(lambda x: (x['symbol'], x['volume']), data.get("returnData", [])))

    def get_balance(self) -> float:
        """
        Returns a float that is a current balance in the main currency
        :return: float
        """
        self.check_connection()
        data = self.client.make_call("getMarginLevel")

        if not data.get("status"):
            raise XTBDataNotFoundError("GET MARGIN LEVEL", data)

        return data.get("returnData", {}).get("balance")
