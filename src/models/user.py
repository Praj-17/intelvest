# app/models.py
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserModel(BaseModel):
    id: str
    email: Optional[EmailStr] = None
    number: Optional[str] = None
    password: str =None
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
