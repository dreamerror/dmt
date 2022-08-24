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


async def authenticate(email: str, password: str):
    users_db = server.get_or_create_db("users_db")
    email_selector = SelectorElement("email")
    email_selector == email
    selector = Selector()
    selector.add_elements(email_selector)
    user = await users_db.find_docs(selector)
    if user:
        return check_password(password, user[0]["hashed_pw"])
    return False


@router.post("/signup", status_code=201)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    is_auth = await authenticate(form_data.username, form_data.password)
    if not is_auth:
        raise HTTPException(
            status_code=400,
            detail="Wrong username and/or password"
        )
    return create_jwt(form_data.username, is_superuser=True)
