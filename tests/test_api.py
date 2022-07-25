from fastapi.testclient import TestClient
from faker import Faker

from ..api.api_main import app
from ..api.access_keys import generate_key, validate_key
from ..models.user import User


client = TestClient(app)
fake = Faker()
Faker.seed(0)


def test_simple_get():
    # TODO: убрать этот тест, как бесполезный
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong"}


def test_key_get():
    response = client.get("/key")
    assert response.status_code == 200
    assert validate_key(response.json()["key"])


def test_create_user():
    user = {"email": fake.email(), "access_key": generate_key()}
    response = client.post("/user/register", User(**user).json())
    assert response.status_code == 201
    assert response.json()['email'] == user['email']
