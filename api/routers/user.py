from fastapi import APIRouter
from pydantic import EmailStr

from ...models.user import User

router = APIRouter(
    prefix="/user",
    tags=["user"]
)


@router.get("/{user_id}")
async def get_user_by_id(user_id: int):
    return User(email=EmailStr("example@example.com"), access_key="ACCESS")


@router.post("/register")
async def create_user(user: User):
    return {"email": user.email, "key": user.access_key}


