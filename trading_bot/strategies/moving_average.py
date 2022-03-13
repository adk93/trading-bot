from . import Strategy

import numpy as np

class MovingAverage(Strategy):
    def __init__(self, prices, dates):
        super().__init__(prices, dates)

    def __str__(self):
        return "Moving Average Strategy"

    def moving_average(self, window: int) -> np.ndarray:
        return np.convolve(self.prices, window, 'valid') / window

    def decision(self):
        moving_average = self.moving_average(4)
        return np.all(self.prices[-4:] > moving_average[-1])