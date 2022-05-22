from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_madlib():
    response = client.get("/madlib")
    assert response.status_code == 200
