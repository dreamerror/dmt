from fastapi import FastAPI

from .access_keys import generate_key, validate_key
from .pydantic_models import User


app = FastAPI()


@app.get("/ping")
async def ping():
    # TODO: убрать эту функцию, как бесполезную
    return {"ping": "pong"}


@app.get("/api/key")
async def new_key():
    return {"key": generate_key()}


@app.post("/api/create_user")
async def create_user(user: User):
    return {"email": user.email, "key": user.access_key}
