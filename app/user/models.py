from pydantic import BaseModel, EmailStr
from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime, timezone


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(index=True, unique=True)
    full_name: Optional[str] = None
    hashed_password: str
    disabled: bool | None = None
    created_at: datetime = Field(default_factory= lambda: datetime.now(timezone.utc))
    

class LoginRequest(BaseModel):
    email: EmailStr
    password: str