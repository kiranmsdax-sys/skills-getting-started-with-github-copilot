import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)


def test_signup_activity():
    # Replace with a valid activity name from your app
    activity_name = list(client.get("/activities").json().keys())[0]
    email = "testuser@mergington.edu"
    response = client.post(f"/activities/{activity_name}/signup?email={email}")
    assert response.status_code in (200, 400)  # 400 if already signed up


def test_unregister_activity():
    activity_name = list(client.get("/activities").json().keys())[0]
    email = "testuser@mergington.edu"
    response = client.delete(f"/activities/{activity_name}/unregister?email={email}")
    assert response.status_code in (200, 400)  # 400 if not signed up
