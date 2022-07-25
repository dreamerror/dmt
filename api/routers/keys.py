from fastapi import APIRouter

from ..access_keys import generate_key, validate_key


router = APIRouter(
    prefix="/key",
    tags=["key"]
)


@router.get("/")
async def get_access_key():
    return {"key": generate_key()}


@router.get("/verify")
async def verify_key(key: str):
    return {"key_is_valid": validate_key(key)}
