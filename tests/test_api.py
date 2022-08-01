from fastapi.testclient import TestClient
from faker import Faker

from ..api.api_main import app
from ..api.access_keys import validate_key
from ..models.account import User


client = TestClient(app)
fake = Faker()
Faker.seed(0)


def test_key_get():
    response = client.get("/key")
    assert response.status_code == 200
    assert validate_key(response.json()["key"])


def test_create_user():
    user = {"email": fake.email(), "hashed_password": fake.password()}
    response = client.post("/user/register", User(**user).json())
    assert response.status_code == 201
    assert response.json()['email'] == user['email']


def test_auth():
    pwd = "example"
    email = "example@example.com"
    response = client.post("/auth/signup", {"username": email, "password": pwd})
    assert response.status_code == 201
    new_response = client.get("/user/me", headers={"Authorization": f"Bearer {response.json()['access_token']}"})
    assert new_response.status_code == 200
    assert new_response.json()["email"] == email
