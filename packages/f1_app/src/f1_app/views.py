# views.py
import pandas as pd
from django.shortcuts import render

# Import target functions
from fastf1_extractor.season_stats import (
    get_driver_standings,
    get_constructor_standings,
)


# def home(request):

#     # Get driver standings DataFrame
#     df = get_driver_standings()
#     df2 = get_constructor_standings()

#     # Convert DataFrame to HTML table (Bootstrap styling optional)
#     table_html = df.to_html(classes="table table-striped", index=False)
#     table2_html = df2.to_html(classes="table table-striped", index=False)

#     return render(request, "home.html", {"table": table_html, "table2": table2_html})


def index(request):
    """Index page view."""
    season = request.GET.get("season", 2025)  # default to 2025 if not provided
    grand_prix_list = [
        {
            "name": "Singapore Grand Prix",
            "location": "Singapore, Singapore",
            "date": "Oct 18, 2025",
            "avatar": "img/avatars/avatar1.jpeg",
        },
        # ... add more races ...
    ] * 10  # for example, repeat 10 times

    season_years = [
        2025,
        2024,
        2023,
        2022,
        2021,
        2020,
        2019,
        2018,
        2017,
        2016,
        2015,
        2014,
        2013,
        2012,
        2011,
        2010,
        2009,
        2008,
        2007,
        2006,
        2005,
    ]
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
