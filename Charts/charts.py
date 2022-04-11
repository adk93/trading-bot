# Standard library imports
from typing import List, Tuple
import datetime

# Third party imports
import matplotlib.pyplot as plt


def make_static_chart(chart_data: List[Tuple[List[float], List[datetime.datetime], str]]) -> plt.figure:
    fig, axes = plt.subplots()
    for data in chart_data:
        axes.plot(data[1], data[0], label=data[2])
    axes.legend()
    return plt.show()
