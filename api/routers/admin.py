import jwt
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

import settings
from api.jwt import decode_jwt, get_current_user
from api.db import server
from couchdb import Document
from couchdb.query import Selector, SelectorElement


router = APIRouter(
    prefix="/admin",
    tags=["admin"]
)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/signup")


@router.post("/set_admin")
async def set_user_as_admin(token: str = Depends(oauth2_scheme), username: str = None):
    payload = await get_current_user(token)
    if not payload["is_superuser"]:
        raise HTTPException(
            status_code=401,
            detail="You have no permission to set user as admin"
        )
    users_db = server.get_or_create_db("users_db")
    email_selector = SelectorElement("email")
    email_selector == username
    selector = Selector()
    selector.add_elements(email_selector)
    data = await users_db.find_docs(selector)
    users_db.create_document(Document(_id=data[0]["_id"], username=username, hashed_pw=data[0]["hashed_pw"],
                                      is_admin=True))
    return True
