from pydantic import BaseModel, EmailStr, PaymentCardNumber


class User(BaseModel):
    email: EmailStr
    card: PaymentCardNumber | None = None
    access_key: str

