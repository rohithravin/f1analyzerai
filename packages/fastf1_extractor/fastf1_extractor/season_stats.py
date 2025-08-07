""" Module for retrieving F1 season statistics such as driver and constructor standings."""

import warnings
import pandas as pd
import fastf1_extractor.jolpi_client as jc


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
                "Position Number": entry["position"],
                "Driver Name": f"{entry['Driver']['givenName']} {entry['Driver']['familyName']}",
                "Points": entry["points"],
                "Wins": entry["wins"],
                "Driver Code": entry["Driver"]["code"],
                "Driver Number": entry["Driver"]["permanentNumber"],
                "Driver DOB": entry["Driver"]["dateOfBirth"],
                "Driver Nationality": entry["Driver"]["nationality"],
                "Driver URL": entry["Driver"]["url"],
                "Driver ID": entry["Driver"]["driverId"],
                "Constructor Name": entry["Constructors"][-1]["name"],
                "Constructor Nationality": entry["Constructors"][-1]["nationality"],
                "Constructor URL": entry["Constructors"][-1]["url"],
                "Constructor ID": entry["Constructors"][-1]["constructorId"],
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
                "Position Number": entry["position"],
                "Constructor Name": entry["Constructor"]["name"],
                "Points": entry["points"],
                "Wins": entry["wins"],
                "Constructor Nationality": entry["Constructor"]["nationality"],
                "Constructor URL": entry["Constructor"]["url"],
                "Constructor ID": entry["Constructor"]["constructorId"],
            }
            for entry in data
        ]
    )

    return df
