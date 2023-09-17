import numpy as np
from numpy.typing import ArrayLike
from functools import reduce


def generate_net_zero_series(size: int) -> ArrayLike:
    pos_series = abs(np.random.randn(size // 2))
    neg_series = -1 * pos_series

    if size % 2 == 1:
        neg_series = np.concatenate(neg_series[:-1], neg_series[-1] / 2)
    
    series = np.concatenate((pos_series, neg_series))
    np.random.shuffle(series)
    return series

def generate_data_serieses(size: int) -> tuple["np.ndarray", "np.ndarray"]:
    pos_series = abs(np.random.randn(size // 2))
    neg_series = -1 * pos_series

    if size % 2 == 1:
        neg_series = np.concatenate(neg_series[:-1], neg_series[-1] / 2)
    
    return (pos_series, neg_series)

def accumulate_series(series: "np.ndarray") -> "np.ndarray":
    new_series = reduce(lambda a, s: [*a, a[-1] + s], series, [0])
    new_series.remove(0)
    return new_series

def arrange_series(
        pos_series: "np.ndarray", 
        neg_series: "np.ndarray"
) -> "np.ndarray":
    pos_items = pos_series.tolist()
    neg_items = neg_series.tolist()
    result = []
    while pos_items:
        if np.random.randn() < 0.002:
            number = pos_items.pop()
            result.append(number)
        else:
            if sum(result) <= 0:
                continue
            else:
                number = neg_items.pop()
                result.append(number)
            
    result.extend(neg_items)
    return np.array(result)

    
def normalise_series(series: "np.array[np.float64]"):
    max_value = max(series)
    min_value = min(series)
    factor = max_value - min_value
    return ( series - min_value ) / factor


def pad_series():
    ...



def show_data():
    pass
