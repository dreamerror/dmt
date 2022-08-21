import jwt
import bcrypt as bc
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from fastapi.responses import RedirectResponse

from api.db import server
from api.jwt import create_jwt
from couchdb import Database, Document
from couchdb.query import SelectorElement, Selector
from models.account import UserRegister
import settings

router = APIRouter(
    prefix="/user",
    tags=["user"]
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/signup")


def decode_jwt(token: str):
    return jwt.decode(
        token,
        settings.JWT_SECRET,
        algorithms=[settings.JWT_ALGORITHM]
    )


async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = decode_jwt(token)
    except jwt.PyJWTError:
        raise jwt.PyJWTError
    return payload


@router.get("/me")
async def get_me(token: str = Depends(oauth2_scheme)):
    try:
        payload = decode_jwt(token)
    except jwt.PyJWTError:
        raise jwt.PyJWTError
    return payload


@router.post("/register", status_code=201)
async def create_user(user: UserRegister):
    users_db = server.get_or_create_db("users_db")
    hashed_password = bc.hashpw(user.password.encode("utf-8"), bc.gensalt(12)).decode("utf-8")
    email_selector = SelectorElement("email")
    email_selector == user.username
    selector = Selector()
    selector.add_elements(email_selector)
    data = await users_db.find_docs(selector)
    if len(data) > 0:
        return {"error": "User with this email already exists"}
    server.create_document(users_db, Document(email=user.username, hashed_pw=hashed_password))
    return create_jwt(user.username)
