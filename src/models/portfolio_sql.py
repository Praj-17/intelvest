from sqlalchemy import Column, Integer, String, Date
from src.databaseSQL import Base


class PortfolioAsset(Base):
    __tablename__ = 'portfolio_asset'

    p_asset_id = Column(Integer, primary_key=True)#id: str
    asset_id = Column(Integer, nullable=False)#assets: List[AssetModel]
    user_id = Column(Integer, nullable=False)#user_id: Optional[str] = None
    portfolio_id = Column(Integer, nullable=False)#assets: List[AssetModel]
    type = Column(String(100), nullable=False)#asset_type: AssetType
                                                # class AssetType(str, Enum):
                                                #     stock = 'stock'
                                                #     etf = 'etf'
                                                #     mutual_fund = 'mutual_fund'
    shares_quantity = Column(Integer, nullable=False)#quantity: float = 0.0
    purchase_price = Column(String(50), nullable=False)#purchase_price: Optional[float] = None
    current_price = Column(String(50), nullable=False)#
    profit_loss = Column(String(50), nullable=False)#
    added_on = Column(Date, nullable=False)#

