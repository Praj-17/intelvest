from datetime import datetime
from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from src.models  import AssetModel

class PortfolioCreate(BaseModel):
    user_id: Optional[str] = None
    assets: List[AssetModel]

class PortfolioUpdate(BaseModel):
    assets: Optional[List[AssetModel]]

class PortfolioOut(BaseModel):
    id: str
    user_id: Optional[str] = None
    assets: List[AssetModel]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
