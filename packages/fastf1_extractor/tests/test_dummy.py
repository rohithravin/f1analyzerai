"This file is part of the f1analyzerai project."
import pytest
from fastf1_extractor.dummy import dummy_add, dummy_subtract


@pytest.mark.parametrize(
    "value_a, value_b, expected",
    [(2, 3, 5), (-1, 1, 0), (0, 0, 0), (10, 5, 15), (-5, -5, -10)],
)
def test_dummy_add_parametrized(value_a, value_b, expected):
    """Test the dummy_add function with parametrization."""
    assert dummy_add(value_a, value_b) == expected


@pytest.mark.parametrize(
    "value_a, value_b, expected",
    [(2, 3, -1), (-1, 1, -2), (0, 0, 0), (10, 5, 5), (-5, -5, 0)],
)
def test_dummy_subtract_parametrized(value_a, value_b, expected):
    """Test the dummy_subtract function with parametrization."""
    assert dummy_subtract(value_a, value_b) == expected
