from . import Strategy

import numpy as np

class MovingAverage(Strategy):
    def __init__(self, prices, dates, window: int = 10):
        super().__init__(prices, dates)
        self.window = window

    def __str__(self):
        return "Moving Average Strategy"

    def moving_average(self) -> np.ndarray:
        return np.convolve(self.prices, self.window, 'valid') / self.window

    def should_buy(self) -> bool:
        moving_average = self.moving_average()
        return np.all(self.prices[-self.window:] > moving_average[-1])

    def should_sell(self) -> bool:
        moving_average = self.moving_average()
        return np.all(self.prices[-4:] < moving_average[-1])
