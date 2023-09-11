from functions import generate_net_zero_series
from math import isclose

def test_generate_net_zero_series_should_net_zero():
    series = generate_net_zero_series(10)
    assert abs(sum(series)) < 1e-15


def test_generate_net_zero_series_should_have_length_size():
    series = generate_net_zero_series(20)
    assert len(series) == 20