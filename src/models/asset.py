# app/models.py

from datetime import date
from sqlalchemy import Column, Integer, String, Date, Enum as SQLEnum
from sqlalchemy.ext.declarative import declarative_base
from enum import Enum

Base = declarative_base()

class AssetType(str, Enum):
    stock = 'stock'
    etf = 'etf'
    mutual_fund = 'mutual_fund'
    # Add other asset types as needed

class AssetModel(Base):
    __tablename__ = 'assets'

    p_asset_id = Column(Integer, primary_key=True, autoincrement=True)
    asset_id = Column(Integer, default=0)
    user_id = Column(Integer, nullable=False)
    portfolio_id = Column(Integer, nullable=False)
    asset_type = Column(SQLEnum(AssetType), nullable=False)
    symbol = Column(String(50), nullable=False)
    purchase_date = Column(Date, nullable=False)
    quantity = Column(Integer, nullable=False)
    purchase_price = Column(String(20), nullable=False)
    added_on = Column(Date, default=date.today)

    def to_dict(self):
        return {
            "p_asset_id": self.p_asset_id,
            "asset_id": self.asset_id,
            "user_id": self.user_id,
            "portfolio_id": self.portfolio_id,
            "asset_type": self.asset_type.value,
            "symbol": self.symbol,
            "purchase_date": self.purchase_date.isoformat(),
            "quantity": self.quantity,
            "purchase_price": self.purchase_price,
            "added_on": self.added_on.isoformat(),
        }
