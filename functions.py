import numpy as np
from numpy.typing import ArrayLike
from functools import reduce
from dataclasses import dataclass


@dataclass
class NormaliseFactor:
    min: float
    factor: float


def generate_data_serieses(size: int) -> tuple["np.ndarray", "np.ndarray"]:
    """
    generate a positive and negative series
    """
    pos_series = abs(np.random.randn(size // 2))
    neg_series = -1 * pos_series

    if size % 2 == 1:
        neg_series = np.append(neg_series[:-1], (neg_series[-1], neg_series[-1]))

    return (pos_series, neg_series)


def accumulate_series(series: "np.ndarray") -> "np.ndarray":
    new_series = reduce(lambda a, s: [*a, a[-1] + s], series, [0])
    new_series.remove(0)
    return new_series


def arrange_series(pos_series: "np.ndarray", neg_series: "np.ndarray") -> "np.ndarray":
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


def normalise_factor(series: "np.array[np.float64]") -> NormaliseFactor:
    max_value = max(series)
    min_value = min(series)
    factor = max_value - min_value
    return NormaliseFactor(min_value, factor)


def normalise_series(series: "np.array[np.float64]") -> "np.array[np.float64]":
    mf = normalise_factor(series)
    return (series - mf.min) / mf.factor


def pad_series(
    series: "np.array[np.float64]", left_size: int, right_size: int
) -> "np.array[np.float64]":
    left = abs(np.random.randn(left_size))
    right = abs(np.random.randn(right_size))
    return np.concatenate((left, series, right))


def generate_line_sereis(m: float, c: float, length: int) -> np.array:
    return np.multiply(m, np.arange(length)) + c


def transform_series(series: np.array, line: np.array) -> np.array:
    """
    incline the series
    """
    return series + line


def show_data():
    pass
