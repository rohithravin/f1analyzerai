import pytest
from fastf1_extractor.dummy import dummy_add, dummy_subtract


def test_dummy_add():
    """Test the dummy_add function."""
    assert dummy_add(2, 3) == 5
    assert dummy_add(-1, 1) == 0
    assert dummy_add(0, 0) == 0

def test_dummy_subtract():
    """Test the dummy_subtract function."""
    assert dummy_subtract(2, 3) == -1
    assert dummy_subtract(-1, 1) == -2
    assert dummy_subtract(0, 0) == 0
