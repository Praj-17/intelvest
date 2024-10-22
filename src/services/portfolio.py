# app/services/portfolio_service.py

from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession

from src.CRUD import CRUDPortfolio
from src.schemas import PortfolioCreate, PortfolioUpdate
from src.models import PortfolioModel
# Assuming PortfolioUtils is still relevant; otherwise, you can remove it.
from src.utils import PortfolioUtils
from .asset import AssetService

class PortfolioService:
    def __init__(self):
        self.crud = CRUDPortfolio()
        self.utils = PortfolioUtils()
        self.assets = AssetService()

    async def create_portfolio(self, db: AsyncSession, data: PortfolioCreate) -> PortfolioModel:
        return await self.crud.create_portfolio(db, data)

    async def read_portfolio(self, db: AsyncSession, p_id: int) -> Optional[PortfolioModel]:
        return await self.crud.get_portfolio(db, p_id)

    async def update_portfolio(self, db: AsyncSession, p_id: int, data: PortfolioUpdate) -> Optional[PortfolioModel]:
        return await self.crud.update_portfolio(db, p_id, data)

    async def delete_portfolio(self, db: AsyncSession, p_id: int) -> bool:
        return await self.crud.delete_portfolio(db, p_id)

    async def read_all_portfolios(self, db: AsyncSession, skip: int = 0, limit: int = 10) -> List[PortfolioModel]:
        return await self.crud.list_portfolios(db, skip=skip, limit=limit)

    async def get_portfolios_by_user(self, db: AsyncSession, user_id: int) -> List[PortfolioModel]:
        return await self.crud.get_portfolios_by_user(db, user_id)

    async def list_all_portfolio_ids(self, db: AsyncSession) -> Optional[List[int]]:
        return await self.crud.list_all_portfolio_ids(db)
    async def read_portfolio_with_assets(self, db: AsyncSession, p_id: int) -> Optional[PortfolioModel]:
        portfolio = await self.read_portfolio(db, p_id)
        assets  = await self.assets.get_assets_by_portfolio(db, portfolio_id=p_id)
        portfolio = portfolio.to_dict()
        portfolio["assets"] = assets
        return portfolio
    
