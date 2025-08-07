from sqlmodel import SQLModel
from pydantic import EmailStr

class UserBase(SQLModel):
    email: EmailStr
    full_name: str | None = None


class UserCreate(UserBase):
    password: str