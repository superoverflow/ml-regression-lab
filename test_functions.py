from functions import generate_net_zero_series, arrange_series, accumulate_series
import numpy as np

def test_generate_net_zero_series_should_net_zero():
    series = generate_net_zero_series(10)
    assert abs(sum(series)) < 1e-15


def test_generate_net_zero_series_should_have_length_size():
    series = generate_net_zero_series(20)
    assert len(series) == 20


def test_arrange_series_should_sum_to_zero():
    pos_series = np.array([0.1,  0.2, 0.3])
    neg_series = np.array([-0.3, -0.1, -0.2])
    result = arrange_series(pos_series, neg_series)
    assert abs(sum(result)) < 1e-15

def test_arrange_series_should_always_greater_than_zero():
    pos_series = np.array([0.1,  0.2, 0.3])
    neg_series = np.array([-0.3, -0.1, -0.2])
    arranged_series = arrange_series(pos_series, neg_series)
    result = accumulate_series(arranged_series)
    assert any(item > 0 for item in result)
