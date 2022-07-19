from pydantic import BaseModel, EmailStr


class User(BaseModel):
    email: EmailStr
    access_key: str
