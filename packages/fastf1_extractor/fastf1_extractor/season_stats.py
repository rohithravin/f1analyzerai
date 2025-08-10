""" Module for retrieving F1 season statistics such as driver and constructor standings."""

import warnings
import pandas as pd
import fastf1_extractor.jolpi_client as jc


def get_season_rounds(season=2025):
    """Get the list of race rounds for a specific season.

    Parameters
    ----------
    season : int, optional
        The F1 season year to retrieve rounds for, by default 2025

    Returns
    -------
    list
        A list of race round names for the specified season
    """
    data = jc.get_season_rounds(season)
    if not data:
        warnings.warn(
            "No data returned from Jolpi API for "
            "fastf1_extractor.jolpi_client.get_season_rounds()",
            UserWarning,
        )
        return None

    df = pd.DataFrame(
        [
            {
                "Round": entry["round"],
                "RaceName": entry["raceName"],
                "CircuitID": entry["Circuit"]["circuitId"],
                "Locality": entry["Circuit"]["Location"]["locality"],
                "Country": entry["Circuit"]["Location"]["country"],
                "Date": entry["date"],
            }
            for entry in data
        ]
    )

    return df


def get_driver_standings(season: int = 2025):
    """Get driver standings for a specific season.

    Parameters
    ----------
    season : int, optional
        The F1 season year to retrieve standings for, by default 2025

    Returns
    -------
    pd.DataFrame
        A DataFrame containing driver standings information
    """
    data = jc.get_driver_standings(season)
    if not data:
        warnings.warn(
            "No data returned from Jolpi API for "
            "fastf1_extractor.jolpi_client.get_driver_standings()",
            UserWarning,
        )
        return None

    df = pd.DataFrame(
        [
            {
                "PositionNumber": entry["position"],
                "DriverName": f"{entry['Driver']['givenName']} {entry['Driver']['familyName']}",
                "Points": entry["points"],
                "Wins": entry["wins"],
                "DriverCode": entry["Driver"]["code"],
                "DriverNumber": entry["Driver"]["permanentNumber"],
                "DriverDOB": entry["Driver"]["dateOfBirth"],
                "DriverNationality": entry["Driver"]["nationality"],
                "DriverURL": entry["Driver"]["url"],
                "DriverID": entry["Driver"]["driverId"],
                "ConstructorName": entry["Constructors"][-1]["name"],
                "ConstructorNationality": entry["Constructors"][-1]["nationality"],
                "ConstructorURL": entry["Constructors"][-1]["url"],
                "ConstructorID": entry["Constructors"][-1]["constructorId"],
            }
            for entry in data
        ]
    )

    return df


def get_constructor_standings(season: int = 2025):
    """Get constructor standings for a specific season.

    Parameters
    ----------
    season : int, optional
        The F1 season year to retrieve standings for, by default 2025

    Returns
    -------
    pd.DataFrame
        A DataFrame containing constructor standings information
    """
    data = jc.get_constructor_standings(season)
    if not data:
        warnings.warn(
            "No data returned from Jolpi API for "
            "fastf1_extractor.jolpi_client.get_constructor_standings()",
            UserWarning,
        )
        return None

    df = pd.DataFrame(
        [
            {
                "PositionNumber": entry["position"],
                "ConstructorName": entry["Constructor"]["name"],
                "Points": entry["points"],
                "Wins": entry["wins"],
                "ConstructorNationality": entry["Constructor"]["nationality"],
                "ConstructorURL": entry["Constructor"]["url"],
                "ConstructorID": entry["Constructor"]["constructorId"],
            }
            for entry in data
        ]
    )

    return df
