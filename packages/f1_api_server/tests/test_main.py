""" Test cases for the F1 API Server endpoints."""

import pytest
from fastapi.testclient import TestClient
from f1_api_server.main import app

client = TestClient(app)


def test_root():
    """Test the root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "F1 API Server is live!"}


@pytest.mark.parametrize(
    "endpoint",
    [
        "/constructor_standings?year=2025",
        "/constructor_standings",
    ],
)
def test_constructor_standings_endpoint(endpoint):
    """Test the constructor standings endpoint structure and content."""
    response = client.get(endpoint)
    assert response.status_code == 200

    json_data = response.json()
    assert "data" in json_data
    data = json_data["data"]

    expected_keys = {
        "Position Number",
        "Constructor Name",
        "Points",
        "Wins",
        "Constructor Nationality",
        "Constructor URL",
        "Constructor ID",
    }

    assert set(data.keys()) == expected_keys

    num_entries = len(data["Constructor Name"])
    for key in expected_keys:
        assert len(data[key]) == num_entries
