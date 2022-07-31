import bcrypt as bc
import jwt
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import EmailStr

from models.account import User
import api.settings as settings

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


@router.get("/{user_id}")
async def get_user_by_id(user_id: int):
    return User(email=EmailStr("example@example.com"), hashed_password="example_pass")


@router.get("/me")
async def get_me(token: str = Depends(oauth2_scheme)):
    try:
        payload = decode_jwt(token)
    except jwt.PyJWTError:
        raise jwt.PyJWTError
    return payload


@router.post("/register", response_model=User, status_code=201)
async def create_user(user: User):
    return user
