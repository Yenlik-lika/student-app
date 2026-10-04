from app import app, average_score


def test_index():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert b"Student Personal Account" in response.data


def test_profile():
    response = app.test_client().get("/profile")
    assert response.status_code == 200
    assert response.json["group"] == "IS-41"


def test_grades_endpoint():
    response = app.test_client().get("/grades")
    assert response.status_code == 200
    assert len(response.json["grades"]) == 3
    assert response.json["average"] == 85.0


def test_average_score():
    assert average_score([{"score": 90}, {"score": 80}, {"score": 70}]) == 80.0


def test_average_score_empty():
    assert average_score([]) == 0


def test_health():
    response = app.test_client().get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "ok"
