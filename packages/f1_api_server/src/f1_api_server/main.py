from fastapi import FastAPI
from fastf1_extractor.season_stats import (
    get_constructor_standings,
)  # adjust based on your structure

app = FastAPI()


@app.get("/")
def root():
    """Root endpoint to check if the server is running."""
    return {"message": "F1 API Server is live!"}


@app.get("/constructor_standings")
def constructor_standings_endpoint(year: int = 2025):
    """Get constructor standings for a specific year.

    Parameters
    ----------
    year : int, optional
        The F1 season year to retrieve standings for, by default 2025

    Returns
    -------
    list[dict]
        A list of dictionaries containing constructor standings information
    """
    standings = get_constructor_standings(year)
    if standings is None:
        return {"message": "No data available for the requested year."}
    return {"data": standings}
