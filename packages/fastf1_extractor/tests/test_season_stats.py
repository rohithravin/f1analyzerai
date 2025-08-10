""" Unit tests for season statistics functions in fastf1_extractor package."""

from unittest.mock import patch
import warnings
import pytest
import pandas as pd

# Import target functions
from fastf1_extractor.season_stats import (
    get_driver_standings,
    get_constructor_standings,
)

# ---------------- Mock Responses ---------------- #

mock_driver_data = [
    {
        "position": "1",
        "points": "284",
        "wins": "6",
        "Driver": {
            "driverId": "piastri",
            "permanentNumber": "81",
            "code": "PIA",
            "url": "http://en.wikipedia.org/wiki/Oscar_Piastri",
            "givenName": "Oscar",
            "familyName": "Piastri",
            "dateOfBirth": "2001-04-06",
            "nationality": "Australian",
        },
        "Constructors": [
            {
                "constructorId": "mclaren",
                "url": "http://en.wikipedia.org/wiki/McLaren",
                "name": "McLaren",
                "nationality": "British",
            }
        ],
    }
]

mock_constructor_data = [
    {
        "position": "1",
        "points": "559",
        "wins": "11",
        "Constructor": {
            "constructorId": "mclaren",
            "url": "http://en.wikipedia.org/wiki/McLaren",
            "name": "McLaren",
            "nationality": "British",
        },
    }
]

# ---------------- Driver Standings Tests ---------------- #


@patch(
    "fastf1_extractor.jolpi_client.get_driver_standings", return_value=mock_driver_data
)
def test_get_driver_standings_success(mock_jc):
    """Test successful retrieval of driver standings."""
    df = get_driver_standings()
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (1, 14)
    assert df.iloc[0]["DriverName"] == "Oscar Piastri"
    assert df.iloc[0]["ConstructorID"] == "mclaren"
    mock_jc.assert_called_once()


@patch("fastf1_extractor.jolpi_client.get_driver_standings", return_value=None)
def test_get_driver_standings_none(mock_jc):
    """Test handling of None response from Jolpi API."""
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        result = get_driver_standings()
        assert result is None
        assert any("No data returned from Jolpi API" in str(warn.message) for warn in w)
        mock_jc.assert_called_once()


@patch("fastf1_extractor.jolpi_client.get_driver_standings", return_value=[])
def test_get_driver_standings_empty_list(mock_jc):
    """Test handling of empty list response from Jolpi API."""
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        result = get_driver_standings()
        assert result is None
        assert any("No data returned from Jolpi API" in str(warn.message) for warn in w)
        mock_jc.assert_called_once()


# ---------------- Constructor Standings Tests ---------------- #


@patch(
    "fastf1_extractor.jolpi_client.get_constructor_standings",
    return_value=mock_constructor_data,
)
def test_get_constructor_standings_success(mock_jc):
    """Test successful retrieval of constructor standings."""
    df = get_constructor_standings()
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (1, 7)
    assert df.iloc[0]["ConstructorName"] == "McLaren"
    assert df.iloc[0]["Points"] == "559"
    mock_jc.assert_called_once()


@patch("fastf1_extractor.jolpi_client.get_constructor_standings", return_value=None)
def test_get_constructor_standings_none(mock_jc):
    """Test handling of None response from Jolpi API."""
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        result = get_constructor_standings()
        assert result is None
        assert any("No data returned from Jolpi API" in str(warn.message) for warn in w)
        mock_jc.assert_called_once()


@patch("fastf1_extractor.jolpi_client.get_constructor_standings", return_value=[])
def test_get_constructor_standings_empty_list(mock_jc):
    """Test handling of empty list response from Jolpi API."""
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        result = get_constructor_standings()
        assert result is None
        assert any("No data returned from Jolpi API" in str(warn.message) for warn in w)
        mock_jc.assert_called_once()
