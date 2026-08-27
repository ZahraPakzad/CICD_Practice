from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, CI/CD!"}


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_add():
    response = client.get("/add/2/3")
    assert response.status_code == 200
    assert response.json() == {"result": 5}


def test_add_negative_numbers():
    response = client.get("/add/-5/3")
    assert response.status_code == 200
    assert response.json() == {"result": -2}
