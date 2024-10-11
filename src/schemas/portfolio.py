from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum
from .asset import AssetType, AssetCreate, AssetOut, AssetUpdate




class PortfolioCreate(BaseModel):
    user_id: int
    portfolio_name: str
    assets: Optional[List[AssetOut]] = None

    class Config:
        from_attributes = True

class PortfolioUpdate(BaseModel):
    portfolio_name: Optional[str]

    class Config:
        from_attributes = True

class PortfolioOut(BaseModel):
    p_id: int
    user_id: int
    portfolio_name: str
    updated_at: datetime
    created_at: date
    assets: Optional[List[AssetOut]] = None

    class Config:
        from_attributes = True
