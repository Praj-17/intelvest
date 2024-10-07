# app/models.py
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from enum import Enum

class AssetType(str, Enum):
    stock = 'stock'
    etf = 'etf'
    mutual_fund = 'mutual_fund'

class AssetModel(BaseModel):
    symbol: Optional[str] = None
    quantity: float = 0.0
    purchase_price: Optional[float] = None
    purchase_date: Optional[datetime] = None
    asset_type: AssetType  # New field added here
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    
class PortfolioModel(BaseModel):
    id: str
    user_id: Optional[str] = None
    assets: List[AssetModel]
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True

