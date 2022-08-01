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
