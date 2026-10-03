from app import app


def test_index():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert b"Student Information System" in response.data


def test_courses():
    response = app.test_client().get("/courses")
    assert response.status_code == 200
    assert b"DevOps Engineering" in response.data


def test_health():
    response = app.test_client().get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "ok"
