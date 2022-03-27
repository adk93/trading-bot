# Standard library imports
import logging

# Third-party imports

# Local app imports
from .strategies import Strategy
from Exchanges import Exchange


class Trader:
    def __init__(self, exchange: Exchange, trading_strategy: Strategy):
        self.exchange = exchange
        self.trading_strategy = trading_strategy

    def run(self, symbol: str) -> None:
        prices, dates = self.exchange.get_market_data(symbol)
        should_buy = self.trading_strategy.should_buy(prices, dates)
        should_sell = self.trading_strategy.should_sell(prices, dates)

        if should_buy:
            logging.info(f"fStrategy {self.trading_strategy} recommends to BUY {symbol}")
            self.exchange.buy(symbol)

        elif should_sell:
            logging.info(f"fStrategy {self.trading_strategy} recommends to SELL {symbol}")
            self.exchange.sell(symbol)

        else:
            print(f"No action needed for {symbol}")
