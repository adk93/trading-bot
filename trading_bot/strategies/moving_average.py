from typing import List, Tuple
from collections import namedtuple

from . import Strategy
from Charts import charts

import numpy as np


class MovingAverage(Strategy):
    def __init__(self, prices, dates, window: int = 10):
        super().__init__(prices, dates)
        self.window = window

    def __str__(self):
        return "Moving Average Strategy"

    def moving_average(self, window: int | None = None) -> np.ndarray:
        window = window if window else self.window
        return np.convolve(self.prices, np.ones(window), 'valid') / window

    def should_buy(self) -> bool:
        moving_average = self.moving_average()
        return np.all(self.prices[-2:] > moving_average[-1])

    def should_sell(self) -> bool:
        moving_average = self.moving_average()
        return np.all(self.prices[-2:] < moving_average[-1])

    def backtesting(self, transaction_cost: float = .0019, window_min: int = 10, window_max: int = 180,
                    window_step: int = 20) -> List[namedtuple]:

        backtesting_result = namedtuple('BacktestingResult', ["name", "parameter", "result"])
        backtesting_data: List[backtesting_result] = []

        for window in range(window_min, window_max, window_step):
            ma = self.moving_average(window)

            # Starting portfolio balance
            balance_pln = 100
            balance_stock = 0
            in_stock = False

            prices = self.prices[window-1:]

            for day in range(len(prices)):

                if (day-2) < 0:
                    continue

                current_prices = prices[day - 2:day]
                ma_last = ma[day - 1]

                today_price = prices[day]

                if np.all(current_prices > ma_last) and not in_stock:
                    balance_stock = balance_pln // today_price
                    balance_pln = balance_pln - balance_stock * today_price
                    in_stock = True
                elif np.all(current_prices < ma_last) and in_stock:
                    balance_pln = balance_pln + today_price * balance_stock
                    balance_stock = 0
                    in_stock = False

            result = backtesting_result(f"MA_{window}", window ,balance_pln + balance_stock * today_price)
            backtesting_data.append(result)

        return backtesting_data

    def calibrate(self) -> List[namedtuple]:
        backtesting_data = self.backtesting()

        backtesting_data.sort(key=lambda x: x.result, reverse=True)

        parameter = backtesting_data[0].parameter
        self.window = parameter

        return backtesting_data
