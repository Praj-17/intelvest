# app/schemas.py
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserCreate(BaseModel):
    email: Optional[EmailStr] = None
    number: Optional[str] = None
    password: str = None

class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    number: Optional[str] = None
    password: str = None

class UserOut(BaseModel):
    id: str
    email: Optional[EmailStr] = None
    number: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

# ---ak---
class Login(UserOut):
    username:str
    password:str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
# --------