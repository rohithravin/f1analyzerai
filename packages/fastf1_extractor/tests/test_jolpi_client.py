""" Unit tests for Jolpi client functions in fastf1_extractor package."""

from unittest.mock import patch
import pytest
from requests.exceptions import RequestException
from fastf1_extractor.jolpi_client import (
    get_driver_standings,
    get_constructor_standings,
    make_get_request,
)

# --- Mock Responses --- #

# Successful driver standings response
mock_driver_response = {
    "MRData": {
        "total": "2",
        "StandingsTable": {
            "StandingsLists": [
                {
                    "DriverStandings": [
                        {
                            "position": "1",
                            "points": "284",
                            "wins": "6",
                            "Driver": {
                                "driverId": "piastri",
                                "givenName": "Oscar",
                                "familyName": "Piastri",
                            },
                            "Constructors": [{"name": "McLaren"}],
                        },
                        {
                            "position": "2",
                            "points": "275",
                            "wins": "5",
                            "Driver": {
                                "driverId": "norris",
                                "givenName": "Lando",
                                "familyName": "Norris",
                            },
                            "Constructors": [{"name": "McLaren"}],
                        },
                    ]
                }
            ]
        },
    }
}

# Successful constructor standings response
mock_constructor_response = {
    "MRData": {
        "StandingsTable": {
            "StandingsLists": [
                {
                    "ConstructorStandings": [
                        {
                            "position": "1",
                            "points": "559",
                            "wins": "11",
                            "Constructor": {"name": "McLaren"},
                        }
                    ]
                }
            ]
        }
    }
}

# Empty standings
mock_empty_standings = {
    "MRData": {"total": "0", "StandingsTable": {"StandingsLists": []}}
}

# Malformed response (missing StandingsLists)
mock_malformed_response = {"MRData": {"total": "10", "StandingsTable": {}}}

# --- Tests --- #


@patch(
    "fastf1_extractor.jolpi_client.make_get_request", return_value=mock_driver_response
)
def test_get_driver_standings_success(mock_get):
    """Test successful retrieval of driver standings."""
    standings = get_driver_standings(2025)
    assert standings is not None
    assert len(standings) == 2
    assert standings[0]["Driver"]["givenName"] == "Oscar"
    assert standings[1]["Driver"]["driverId"] == "norris"
    mock_get.assert_called()


@patch(
    "fastf1_extractor.jolpi_client.make_get_request",
    return_value=mock_constructor_response,
)
def test_get_constructor_standings_success(mock_get):
    """Test successful retrieval of constructor standings."""
    standings = get_constructor_standings(2025)
    assert standings is not None
    assert len(standings) == 1
    assert standings[0]["Constructor"]["name"] == "McLaren"
    mock_get.assert_called()


@patch(
    "fastf1_extractor.jolpi_client.make_get_request", return_value=mock_empty_standings
)
def test_get_driver_standings_empty(mock_get):
    """Test handling of empty driver standings response."""
    standings = get_driver_standings(2025)
    assert standings is None


@patch(
    "fastf1_extractor.jolpi_client.make_get_request",
    return_value=mock_malformed_response,
)
def test_get_driver_standings_malformed(mock_get):
    """Test handling of malformed driver standings response."""
    standings = get_driver_standings(2025)
    assert standings is None


@patch(
    "fastf1_extractor.jolpi_client.make_get_request",
    return_value=mock_malformed_response,
)
def test_get_constructor_standings_malformed(mock_get):
    """Test handling of malformed constructor standings response."""
    standings = get_constructor_standings(2025)
    assert standings == []


@patch(
    "fastf1_extractor.jolpi_client.requests.get",
    side_effect=RequestException("Network error"),
)
def test_make_get_request_network_error(mock_get):
    """Test handling of network errors in make_get_request."""
    result = make_get_request("/2025/driverstandings/")
    assert result is None
    mock_get.assert_called()


@patch("fastf1_extractor.jolpi_client.requests.get")
def test_make_get_request_bad_json(mock_get):
    """Test handling of bad JSON response in make_get_request."""
    mock_get.return_value.status_code = 200
    mock_get.return_value.raise_for_status = lambda: None
    mock_get.return_value.json = lambda: (_ for _ in ()).throw(
        ValueError("Invalid JSON")
    )

    result = make_get_request("/2025/constructorstandings/")
    assert result is None
