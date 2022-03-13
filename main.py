from xtb_api.xtb_api import XTBClient
import matplotlib.pyplot as plt
from dotenv import dotenv_values
from datetime import datetime
from trading_bot import trader


from trading_bot.strategies.moving_average import MovingAverage

config = dotenv_values(".env")

USERID = config['USERID']
PASSWORD = config["PASSWORD"]

xtb = XTBClient(USERID, PASSWORD)
xtb.login()

data = xtb.make_call("getChartLastRequest", {"info":{"period": 5,
                                              "symbol": "EURPLN",
                                              "start": 1646995035000}})

if data['status']:
    r_data = data['returnData']['rateInfos']

    bot = trader.Trader.from_xtbapi("EURPLN", r_data)
    bot.add_strategies(MovingAverage)

    print(bot.read_strategies)

    bot.get_decisions()

    print(bot.prices)


