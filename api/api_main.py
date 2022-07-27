from fastapi import FastAPI

from .routers import user, keys

app = FastAPI()

app.include_router(user.router)
app.include_router(keys.router)
