from typing import Optional, List
from motor.motor_asyncio import AsyncIOMotorDatabase

from src.CRUD import CRUDPortfolio
from src.schemas import PortfolioCreate, PortfolioUpdate
from src.models import PortfolioModel

class PortfolioService:
    def __init__(self, db: AsyncIOMotorDatabase):
        self.crud = CRUDPortfolio(db.portfolios)

    async def create_portfolio(self, data: PortfolioCreate) -> PortfolioModel:
        return await self.crud.create_portfolio(data)

    async def read_portfolio(self, portfolio_id: str) -> Optional[PortfolioModel]:
        return await self.crud.get_portfolio(portfolio_id)

    async def update_portfolio(self, portfolio_id: str, data: PortfolioUpdate) -> Optional[PortfolioModel]:
        return await self.crud.update_portfolio(portfolio_id, data)

    async def delete_portfolio(self, portfolio_id: str) -> bool:
        return await self.crud.delete_portfolio(portfolio_id)

    async def read_all_portfolios(self, skip: int = 0, limit: int = 10) -> List[PortfolioModel]:
        return await self.crud.list_portfolios(skip=skip, limit=limit)

    async def get_portfolios_by_user(self, user_id: str) -> List[PortfolioModel]:
        return await self.crud.get_portfolios_by_user(user_id)

    async def list_all_portfolio_ids(self) -> Optional[List[str]]:
        portfolio_ids = await self.crud.list_all_portfolio_ids()
        if portfolio_ids:
            return [str(portfolio_id) for portfolio_id in portfolio_ids]
        return None
