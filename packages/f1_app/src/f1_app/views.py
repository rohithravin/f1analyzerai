# views.py
import pandas as pd
from django.shortcuts import render

# Import target functions
from fastf1_extractor.season_stats import (
    get_driver_standings,
    get_constructor_standings,
)


def home(request):

    # Get driver standings DataFrame
    df = get_driver_standings()
    df2 = get_constructor_standings()

    # Convert DataFrame to HTML table (Bootstrap styling optional)
    table_html = df.to_html(classes="table table-striped", index=False)
    table2_html = df2.to_html(classes="table table-striped", index=False)

    return render(request, "home.html", {"table": table_html, "table2": table2_html})
