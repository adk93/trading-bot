# Standard library imports
import logging

# Third-party imports

# Local app imports
from .strategies import Strategy
from Exchanges import Exchange
from Charts import charts


def print_backtesting_data(backtesting_data) -> None:
    for data in backtesting_data:
        print(f"Strategy {data.name} generated return at {data.result}%")


class Trader:
    def __init__(self, exchange: Exchange, trading_strategy: Strategy):
        self.exchange = exchange
        self.trading_strategy = trading_strategy

    def run(self, symbol: str) -> None:
        current_portfolio = self.exchange.get_trades()
        current_balance = self.exchange.get_balance()
        print(f"Current Balance: {current_balance}")
        prices, dates = self.exchange.get_market_data(symbol)

        trading_strategy = self.trading_strategy(prices, dates)
        trading_strategy.calibrate()

        should_buy = trading_strategy.should_buy()
        should_sell = trading_strategy.should_sell()

        if should_buy and symbol not in map(lambda x: x[0], current_portfolio):
            logging.info(f"fStrategy {trading_strategy} recommends to BUY {symbol}")
            self.exchange.buy(symbol)

        elif should_sell:
            logging.info(f"fStrategy {trading_strategy} recommends to SELL {symbol}")
            self.exchange.sell(symbol)

        else:
            print(f"No action needed for {symbol}")
