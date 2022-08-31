from fastapi import FastAPI

from .routers import user, keys, auth, admin

app = FastAPI()

app.include_router(user.router)
app.include_router(keys.router)
app.include_router(auth.router)
app.include_router(admin.router)
