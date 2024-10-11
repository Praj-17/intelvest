# app/crud_portfolio.py

from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from datetime import datetime, date

from src.schemas import PortfolioCreate, PortfolioUpdate
from src.models import PortfolioModel
from sqlalchemy.exc import NoResultFound

class CRUDPortfolio:
    def __init__(self):
        pass  # No need to initialize with a collection or session

    async def create_portfolio(self, db: AsyncSession, portfolio: PortfolioCreate) -> PortfolioModel:
        new_portfolio = PortfolioModel(
            user_id=portfolio.user_id,
            portfolio_name=portfolio.portfolio_name,
            created_at=date.today(),
            updated_at=datetime.now()
        )
        db.add(new_portfolio)
        await db.commit()
        await db.refresh(new_portfolio)
        return new_portfolio

    async def get_portfolio(self, db: AsyncSession, p_id: int) -> Optional[PortfolioModel]:
        result = await db.execute(select(PortfolioModel).where(PortfolioModel.p_id == p_id))
        portfolio = result.scalar_one_or_none()
        return portfolio

    async def update_portfolio(self, db: AsyncSession, p_id: int, portfolio: PortfolioUpdate) -> Optional[PortfolioModel]:
        result = await db.execute(select(PortfolioModel).where(PortfolioModel.p_id == p_id))
        existing_portfolio = result.scalar_one_or_none()
        if not existing_portfolio:
            return None

        update_data = portfolio.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(existing_portfolio, key, value)
        existing_portfolio.updated_at = datetime.now()
        await db.commit()
        await db.refresh(existing_portfolio)
        return existing_portfolio

    async def delete_portfolio(self, db: AsyncSession, p_id: int) -> bool:
        result = await db.execute(select(PortfolioModel).where(PortfolioModel.p_id == p_id))
        portfolio = result.scalar_one_or_none()
        if not portfolio:
            return False
        await db.delete(portfolio)
        await db.commit()
        return True

    async def list_portfolios(self, db: AsyncSession, skip: int = 0, limit: int = 10) -> List[PortfolioModel]:
        result = await db.execute(
            select(PortfolioModel).offset(skip).limit(limit)
        )
        portfolios = result.scalars().all()
        return portfolios

    async def get_portfolios_by_user(self, db: AsyncSession, user_id: int) -> List[PortfolioModel]:
        result = await db.execute(
            select(PortfolioModel).where(PortfolioModel.user_id == user_id)
        )
        portfolios = result.scalars().all()
        return portfolios

    async def list_all_portfolio_ids(self, db: AsyncSession) -> Optional[List[int]]:
        result = await db.execute(select(PortfolioModel.p_id))
        portfolio_ids = result.scalars().all()
        if portfolio_ids:
            return portfolio_ids
        return None
