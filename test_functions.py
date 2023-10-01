from functions import (
    generate_data_serieses,
    arrange_series,
    accumulate_series,
    normalise_series,
    transform_series,
    pad_series
)
import numpy as np
from numpy.testing import assert_equal


def test_generate_data_serieses_base():
    pos_seris, neg_series = generate_data_serieses(10)
    total = sum(pos_seris) + sum(neg_series)
    assert abs(total) < 1e-15


def test_arrange_series_should_sum_to_zero():
    pos_series = np.array([0.1, 0.2, 0.3])
    neg_series = np.array([-0.3, -0.1, -0.2])
    result = arrange_series(pos_series, neg_series)
    assert abs(sum(result)) < 1e-15


def test_arrange_series_should_always_greater_than_zero():
    pos_series = np.array([0.1, 0.2, 0.3])
    neg_series = np.array([-0.3, -0.1, -0.2])
    arranged_series = arrange_series(pos_series, neg_series)
    result = accumulate_series(arranged_series)
    assert any(item > 0 for item in result)


def test_normalise_series_base():
    mock_series = np.array([-2, 1, 6, 2])
    result = normalise_series(mock_series)
    expected = np.array([0.0, 0.375, 1.0, 0.5])
    np.testing.assert_almost_equal(result, expected)


def test_pad_series_base():
    result = pad_series(series = np.array([-2, 1, 6, 2]), left_size=3, right_size=2)
    assert len(result) == 9


def test_transform_series_base():
    result = transform_series(series = np.array([-2.0, 1.0, 6.0, 2.2]), line = np.array([1, 2, 3, 4]))
    assert_equal(result, np.array([-1. ,  3. ,  9. ,  6.2]))