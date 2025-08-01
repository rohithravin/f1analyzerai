from fastapi.testclient import TestClient
from f1_api_server.main import app

client = TestClient(app)


def test_root():
    """Test the root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "F1 API Server is live!"}


def test_echo():
    """Test the echo endpoint."""
    response = client.get("/echo")
    assert response.status_code == 200
    assert response.json() == {
        "message": "This is a dummy function that does nothing but print a message."
    }


def test_echo_with_value():
    """Test the echo endpoint with a custom value."""
    custom_value = "Hello, F1!"
    response = client.get(f"/echo?value={custom_value}")
    assert response.status_code == 200
    assert response.json() == {"message": custom_value}
