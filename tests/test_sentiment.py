from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"API": "online"}


def test_sentiment_prediction():
    response = client.post(
        "/sentiment",
        json={"value": "Kill yourself"}
    )
    assert response.status_code == 200
    assert response.json()
    assert response.json()["label"] == "negative"


def test_sentiment_explain():
    response = client.post(
        "/sentiment/explain",
        json={"value": "Kill yourself"}
    )
    assert response.status_code == 200
