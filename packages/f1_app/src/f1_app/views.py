""" Views for the F1 app """

# views.py
from datetime import datetime
import pandas as pd
from django.shortcuts import render

# Import target functions
from fastf1_extractor.season_stats import (
    get_driver_standings,
    get_constructor_standings,
    get_season_rounds,
)


def index(request):
    """Index page view."""
    season = request.GET.get("season", 2025)
    grand_prix_list_raw = get_season_rounds(season).to_dict(orient="records")
    today = datetime.today().date()

    # Add 'is_past' flag
    grand_prix_list = []
    for race in grand_prix_list_raw:
        race_date = datetime.strptime(
            race["Date"], "%Y-%m-%d"
        ).date()  # adapt format if needed
        race["is_past"] = race_date > today
        grand_prix_list.append(race)

    season_years = list(range(2025, 2004, -1))

    return render(
        request,
        "index.html",
        {
            "grand_prix_list": grand_prix_list,
            "current_season": season,
            "season_years": season_years,
        },
    )


def drivers(request):
    """Drivers page view."""
    return render(request, "drivers.html")


def constructors(request):
    """Constructors page view."""
    return render(request, "constructors.html")


def race(request):
    """Race page view."""
    return render(request, "race.html")
