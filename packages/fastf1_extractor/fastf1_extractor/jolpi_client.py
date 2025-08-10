"""Client for Jolpica F1 API."""

import os
from typing import Optional, Dict, Any, List
import logging
from dotenv import load_dotenv
import requests

load_dotenv()

# API base URL, can be overridden via .env
JOLPICA_F1_HOST_URL = os.getenv("JOLPICA_F1_HOST_URL", "https://api.jolpi.ca/ergast/f1")
TIMEOUT_SECONDS = int(os.getenv("JOLPICA_F1_TIMEOUT", "10"))

logger = logging.getLogger(__name__)


def get_season_rounds(season: int = 2025) -> Optional[List[Dict[str, Any]]]:
    """Get the list of rounds for a specific season, handling pagination.

    Parameters
    ----------
    season : int, optional
        The F1 season year to retrieve rounds for, by default 2025

    Returns
    -------
    Optional[List[Dict[str, Any]]]
        A list of dictionaries containing round information
    """
    all_rounds = []
    limit = 30
    offset = 0

    while True:
        endpoint = f"/{season}/races/?limit={limit}&offset={offset}"
        data = make_get_request(endpoint)

        if not data:
            break

        try:
            races = data["MRData"]["RaceTable"]["Races"]
            all_rounds.extend(races)

            total = int(data["MRData"]["total"])
            offset += limit

            if offset >= total:
                break

        except (KeyError, IndexError):
            break

    return all_rounds if all_rounds else None


def get_constructor_standings(season: int = 2025) -> Optional[List[Dict[str, Any]]]:
    """Get constructor standings for a specific season.

    Parameters
    ----------
    season : int, optional
        The F1 season year to retrieve standings for, by default 2025

    Returns
    -------
    Optional[List[Dict[str, Any]]]
        A list of dictionaries containing constructor standings information
    """
    endpoint = f"/{season}/constructorstandings/"
    data = make_get_request(endpoint)

    return (
        data.get("MRData", {})
        .get("StandingsTable", {})
        .get("StandingsLists", [{}])[0]
        .get("ConstructorStandings", [])
        if data
        else None
    )


def get_driver_standings(season: int = 2025) -> Optional[List[Dict[str, Any]]]:
    """Get driver standings for a specific season.

    Parameters
    ----------
    season : int, optional
        The F1 season year to retrieve standings for, by default 2025

    Returns
    -------
    Optional[List[Dict[str, Any]]]
        A list of dictionaries containing driver standings information
    """
    all_standings = []
    limit = 30
    offset = 0

    while True:
        endpoint = f"/{season}/driverstandings/?limit={limit}&offset={offset}"
        data = make_get_request(endpoint)

        if not data:
            break

        try:
            standings_list = data["MRData"]["StandingsTable"]["StandingsLists"][0][
                "DriverStandings"
            ]
            all_standings.extend(standings_list)

            total = int(data["MRData"]["total"])
            offset += limit

            if offset >= total:
                break

        except (KeyError, IndexError):
            # In case of unexpected structure or empty StandingsLists
            break

    return all_standings if all_standings else None


def make_get_request(endpoint: str) -> Optional[Dict[str, Any]]:
    """Make a GET request to the Jolpica API.

    Parameters
    ----------
    endpoint : str
        The API endpoint to request data from.

    Returns
    -------
    Optional[Dict[str, Any]]
        The JSON response from the API or None if the request failed.
    """
    url = f"{JOLPICA_F1_HOST_URL.rstrip('/')}/{endpoint.lstrip('/')}"
    logger.info("GET %s", url)

    try:
        response = requests.get(url, timeout=TIMEOUT_SECONDS)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logger.error("Request failed: %s", e)
        return None
    except ValueError:
        logger.error("Failed to decode JSON response.")
        return None
