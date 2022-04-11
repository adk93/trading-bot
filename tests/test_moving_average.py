import csv
import pytest
from trading_bot.strategies import moving_average
import datetime
from typing import Tuple


def load_test_data(filename: str) -> Tuple:
    prices, dates = [], []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for line_count, row in enumerate(csv_reader):
            if line_count == 0:
                continue
            dates.append(row[0])
            prices.append(row[4])

    dates = list(map(lambda x: datetime.datetime.strptime(x, '%Y-%m-%d'), dates))
    prices = list(map(lambda x: float(x), prices))
    return prices, dates


@pytest.fixture()
def usdpln_data():
    prices, dates = load_test_data("usdpln_mock_data.csv")
    return moving_average.MovingAverage(prices, dates)


def test_backtesting_ma10(usdpln_data):
    backtesting_data = usdpln_data.backtesting()
    ma_10 = list(filter(lambda x: x.name == 'MA_10', backtesting_data))[0]
    assert abs(ma_10.result - 114.66572) < .1
