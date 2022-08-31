import bcrypt as bc
from fastapi import APIRouter, Depends, HTTPException, Header
from fastapi.security import OAuth2PasswordRequestForm

from api.db import server
from api.jwt import create_jwt
from couchdb import Database
from couchdb.query import SelectorElement, Selector


router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


def check_password(entered_password: str, right_password: str):
    return bc.checkpw(entered_password.encode("utf-8"), right_password.encode("utf-8"))


async def authenticate(email: str) -> dict | bool:
    users_db = server.get_or_create_db("users_db")
    email_selector = SelectorElement("email")
    email_selector == email
    selector = Selector()
    selector.add_elements(email_selector)
    user = await users_db.find_docs(selector)
    if user:
        return user[0]
    return False


@router.post("/signup", status_code=201)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate(form_data.username)
    is_auth = check_password(form_data.password, user["hashed_pw"])
    if not is_auth:
        raise HTTPException(
            status_code=400,
            detail="Wrong username and/or password"
        )
    return create_jwt(form_data.username, is_admin=user.get("is_admin", False),
                      is_superuser=user.get("is_superuser", False))
