import jwt
from datetime import datetime, timedelta

import settings


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
