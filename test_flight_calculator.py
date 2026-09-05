import pytest
from flight_calculator import calculate_flight_time


def test_calculate_flight_time_zero_weight():
    assert calculate_flight_time(0) == 180.0


@pytest.mark.parametrize(
    "weight_grams, expected",
    [
        (1, 179.9),
        (10, 179.0),
        (100, 170.0),
        (500, 130.0),
        (1000, 80.0),
        (1800, 0.0),
    ],
)
def test_calculate_flight_time_valid_weights(weight_grams, expected):
    assert calculate_flight_time(weight_grams) == pytest.approx(expected)


@pytest.mark.parametrize(
    "weight_grams, expected",
    [
        (0.5, 179.95),
        (12.5, 178.75),
        (999.9, 80.01),
    ],
)
def test_calculate_flight_time_float_weights(weight_grams, expected):
    assert calculate_flight_time(weight_grams) == pytest.approx(expected)


@pytest.mark.parametrize("weight_grams", [1800.1, 2000, 5000])
def test_calculate_flight_time_clamps_to_zero(weight_grams):
    assert calculate_flight_time(weight_grams) == 0.0


@pytest.mark.parametrize("weight_grams", [-1, -0.01, -100])
def test_calculate_flight_time_rejects_negative_values(weight_grams):
    with pytest.raises(ValueError, match="weight_grams must be non-negative."):
        calculate_flight_time(weight_grams)