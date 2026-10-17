from app import app


def test_home_endpoint():
    response = app.test_client().get("/")

    assert response.status_code == 200
    assert response.get_json()["application"] == "devops-health-api"


def test_health_endpoint():
    response = app.test_client().get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}