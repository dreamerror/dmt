from datetime import datetime, timedelta

import bcrypt as bc
import jwt
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

import api.settings as settings
from api.fake_db import users as USERS


router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


def check_password(entered_password: str, right_password: str):
    return bc.checkpw(entered_password.encode("utf-8"), right_password.encode("utf-8"))


def authenticate(email: str, password: str):
    for user in USERS:
        if user["email"] == email:
            return check_password(password, user["hashed_password"])
    return False


def create_jwt(email: str, is_superuser: bool = False):
    payload = dict()
    payload["email"] = email
    payload["is_superuser"] = is_superuser
    payload["exp"] = datetime.now() + timedelta(minutes=int(settings.JWT_EXPIRE_MINUTES))
    token = jwt.encode(
        payload,
        settings.JWT_SECRET,
        settings.JWT_ALGORITHM
    )
    return {"access_token": token, "token_type": "bearer"}


@router.post("/signup", status_code=201)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    is_auth = authenticate(form_data.username, form_data.password)
    if not is_auth:
        raise HTTPException(
            status_code=400,
            detail="Wrong username and/or password"
        )
    return create_jwt(form_data.username, is_superuser=True)
