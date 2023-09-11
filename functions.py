import numpy as np
from functools import reduce


def generate_data(size: int):
    pass


def generate_net_zero_series(size: int):
    pos_series = abs(np.random.randn(size // 2))
    neg_series = -1 * pos_series

    if size % 2 == 1:
        neg_series = np.concatenate(neg_series[:-1], neg_series[-1] / 2)
    
    series = np.concatenate((pos_series, neg_series))
    np.random.shuffle(series)
    return series

def accumulate_series(series):
    new_series = reduce(lambda a, s: [*a, a[-1] + s], series, [0])
    new_series.remove(0)
    return new_series


def show_data():
    pass
