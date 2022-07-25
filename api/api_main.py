from fastapi import FastAPI

from .access_keys import generate_key, validate_key
from .routers import user, keys
from ..models.user import User


app = FastAPI()

app.include_router(user.router)
app.include_router(keys.router)


@app.get("/ping")
async def ping():
    # TODO: убрать эту функцию, как бесполезную
    return {"ping": "pong"}
