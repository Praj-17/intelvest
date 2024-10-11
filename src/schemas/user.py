# app/schemas.py

from datetime import datetime, date
from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    fname: Optional[str]
    mname: Optional[str]
    lname: Optional[str]
    dob: Optional[date]
    gender: Optional[str]
    course: Optional[str]
    yrlvl: Optional[str]
    username: str
    password: str
    address: Optional[str]
    phone: Optional[str]
    eduboard: Optional[str]
    email: Optional[EmailStr]
    role_id: Optional[int] = 3
    state: Optional[str]
    country: Optional[str]
    pincode: Optional[str]
    device_id: Optional[str] = 'test'
    isJMTUser: Optional[bool] = False
    isActive: Optional[int] = 0

class UserOut(BaseModel):
    user_Id: int
    fname: Optional[str]
    mname: Optional[str]
    lname: Optional[str]
    dob: Optional[date]
    gender: Optional[str]
    course: Optional[str]
    yrlvl: Optional[str]
    username: Optional[str]
    address: Optional[str]
    phone: Optional[str]
    eduboard: Optional[str]
    email: Optional[EmailStr]
    role_id: int
    state: Optional[str]
    country: Optional[str]
    pincode: Optional[str]
    added_on: datetime
    device_id: str
    isJMTUser: bool
    isActive: int

    class Config:
        from_attributes = True

from datetime import datetime, date
from pydantic import BaseModel, EmailStr
from typing import Optional

class UserUpdate(BaseModel):
    fname: Optional[str] = None
    mname: Optional[str] = None
    lname: Optional[str] = None
    dob: Optional[date] = None
    gender: Optional[str] = None
    course: Optional[str] = None
    yrlvl: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = None
    eduboard: Optional[str] = None
    email: Optional[EmailStr] = None
    role_id: Optional[int] = None
    state: Optional[str] = None
    country: Optional[str] = None
    pincode: Optional[str] = None
    device_id: Optional[str] = None
    isJMTUser: Optional[bool] = None
    isActive: Optional[int] = None

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