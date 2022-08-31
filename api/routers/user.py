import jwt
import bcrypt as bc
from fastapi import APIRouter, Depends, Form
from fastapi.security import OAuth2PasswordBearer
from fastapi.responses import RedirectResponse

from api.db import server
from api.jwt import create_jwt, decode_jwt, get_current_user
from couchdb import Database, Document
from couchdb.query import SelectorElement, Selector
from models.account import UserRegister
import settings

router = APIRouter(
    prefix="/user",
    tags=["user"]
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/signup")


@router.get("/me")
async def get_me(token: str = Depends(oauth2_scheme)):
    payload = await get_current_user(token)
    return payload


@router.post("/register", status_code=201)
async def create_user(username: str = Form(), password: str = Form()):
    users_db = server.get_or_create_db("users_db")
    hashed_password = bc.hashpw(password.encode("utf-8"), bc.gensalt(12)).decode("utf-8")
    email_selector = SelectorElement("email")
    email_selector == username
    selector = Selector()
    selector.add_elements(email_selector)
    data = await users_db.find_docs(selector)
    if len(data) > 0:
        return {"error": "User with this email already exists"}
    users_db.create_document(Document(email=username, hashed_pw=hashed_password))
    return RedirectResponse("/auth/signup")
