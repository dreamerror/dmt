from fastapi import APIRouter, Depends
from pydantic import EmailStr

from ...models.user import User

router = APIRouter(
    prefix="/user",
    tags=["user"]
)


async def access_level_params(is_superuser: bool):
    return {"is_superuser": is_superuser}


@router.get("/{user_id}")
async def get_user_by_id(user_id: int):
    return User(email=EmailStr("example@example.com"), access_key="ACCESS")


@router.post("/register", response_model=User, status_code=201)
async def create_user(user: User):
    return user


@router.post("/reg_su", response_model=User, status_code=201)
async def create_superuser(user: User, params: dict = Depends(access_level_params)):
    return user if params["is_superuser"] else {"error": "Permission denied"}

