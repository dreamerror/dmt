import bcrypt as bc
from fastapi import APIRouter, Depends, HTTPException, Header
from fastapi.security import OAuth2PasswordRequestForm

from api.db import server
from api.jwt import create_jwt
from couchdb import Database
from couchdb.query import SelectorElement, Selector


users_db = Database("users_db")

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


def check_password(entered_password: str, right_password: str):
    return bc.checkpw(entered_password.encode("utf-8"), right_password.encode("utf-8"))


def authenticate(email: str, password: str):
    server.get_or_create_db(Database("users_db"))
    email_selector = SelectorElement("email")
    email_selector == email
    selector = Selector()
    selector.add_elements(email_selector)
    user = server.find_docs(users_db, selector)
    if user:
        return check_password(password, user[0]["hashed_pw"])
    return False


@router.post("/signup", status_code=201)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    is_auth = authenticate(form_data.username, form_data.password)
    if not is_auth:
        raise HTTPException(
            status_code=400,
            detail="Wrong username and/or password"
        )
    return create_jwt(form_data.username, is_superuser=True)
