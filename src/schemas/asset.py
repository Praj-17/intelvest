from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import List, Optional
from src.models import AssetType

class AssetCreate(BaseModel):
    asset_id: Optional[int] = 0
    user_id: int
    portfolio_id: int
    asset_type: AssetType
    symbol: str
    purchase_date: date
    quantity: int
    purchase_price: str

    class Config:
        from_attributes = True

class AssetUpdate(BaseModel):
    asset_id: Optional[int]
    asset_type: Optional[AssetType]
    symbol: Optional[str]
    purchase_date: Optional[date]
    quantity: Optional[int]
    purchase_price: Optional[str]

    class Config:
        from_attributes = True

class AssetOut(BaseModel):
    p_asset_id: int
    asset_id: int
    user_id: int
    portfolio_id: int
    asset_type: AssetType
    symbol: str
    purchase_date: date
    quantity: int
    purchase_price: str
    added_on: date

    class Config:
        from_attributes = True