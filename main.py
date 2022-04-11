# Standard library imports
import logging

# Third party imports

# Local application imports
from trading_bot import trader
from trading_bot.strategies.moving_average import MovingAverage
from Exchanges.XTB.xtb_exchange import XTBExchange

logging.basicConfig(filename="applog.log")


def main():
    exchange = XTBExchange()
    exchange.connect()

    bot = trader.Trader(
        exchange=exchange,
        trading_strategy=MovingAverage
    )

    bot.run("EURPLN")

if __name__ == "__main__":
    main()
