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



    def to_dict(self, exclude_none: bool = True, by_alias: bool = False) -> dict:
        """
        Converts the PortfolioModel instance to a dictionary.

        Args:
            exclude_none (bool): If True, fields with value `None` will be excluded from the resulting dict.
            by_alias (bool): If True, use field aliases instead of field names.

        Returns:
            dict: A dictionary representation of the PortfolioModel instance.
        """
        return self.model_dump(exclude_none=exclude_none, by_alias=by_alias)

    def to_custom_dict(self) -> dict:
        """
        Example of a custom dictionary conversion method.
        Modify this method based on your specific requirements.

        Returns:
            dict: A customized dictionary representation of the PortfolioModel instance.
        """
        return {
            "id": self.id,
            "user_id": self.user_id,
            "assets": [asset.model_dump() for asset in self.assets],
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

