import jwt
from datetime import datetime, timedelta

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

import settings


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/signup")


def create_jwt(email: str, is_admin: bool = False, is_superuser: bool = False):
    payload = dict()
    payload["email"] = email
    payload["is_admin"] = is_admin
    payload["is_superuser"] = is_superuser
    payload["exp"] = datetime.now() + timedelta(minutes=int(settings.JWT_EXPIRE_MINUTES))
    token = jwt.encode(
        payload,
        settings.JWT_SECRET,
        settings.JWT_ALGORITHM
    )
    return {"access_token": token, "token_type": "bearer"}


def decode_jwt(token: str):
    return jwt.decode(
        token,
        settings.JWT_SECRET,
        algorithms=[settings.JWT_ALGORITHM]
    )


async def get_current_user(token: str):
    try:
        payload = decode_jwt(token)
    except jwt.PyJWTError:
        raise jwt.PyJWTError
    return payload


async def user_has_permission(token: str, permission: str):
    try:
        payload = decode_jwt(token)
        if not payload[f"is_{permission}"]:
            return False
        else:
            return True
    except jwt.PyJWTError:
        raise jwt.PyJWTError
