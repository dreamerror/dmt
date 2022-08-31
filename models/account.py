from typing import List

from pydantic import BaseModel, EmailStr, PaymentCardNumber, Json

from .simulation import Simulation


class Company(BaseModel):
    name: str
    paid: bool = False
    active_simulations: List[Simulation] | Json[List[Simulation]] | None = None


class User(BaseModel):
    email: EmailStr
    card: PaymentCardNumber | None = None
    hashed_password: str
    company: Company | None = None
    is_admin: bool = False
    is_superuser: bool = False


class UserRegister(BaseModel):
    username: EmailStr
    password: str


class DatabaseUser(BaseModel):
    username: str
    password: str

