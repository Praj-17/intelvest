from typing import List, Optional
from motor.motor_asyncio import AsyncIOMotorCollection
from datetime import datetime
import uuid

from src.schemas import PortfolioCreate, PortfolioUpdate
from src.models import PortfolioModel

class CRUDPortfolio:
    def __init__(self, collection: AsyncIOMotorCollection):
        self.collection = collection

    async def create_portfolio(self, portfolio: PortfolioCreate) -> PortfolioModel:
        portfolio_dict = portfolio.dict()
        portfolio_dict["created_at"] = datetime.now()
        portfolio_dict["updated_at"] = datetime.now()
        portfolio_dict["_id"] = str(uuid.uuid4())
        await self.collection.insert_one(portfolio_dict)
        portfolio_dict["id"] = portfolio_dict.pop("_id")
        return PortfolioModel(**portfolio_dict)

    async def get_portfolio(self, portfolio_id: str) -> Optional[PortfolioModel]:
        document = await self.collection.find_one({"_id": portfolio_id})
        if document:
            document["id"] = document.pop("_id")
            return PortfolioModel(**document)
        return None

    async def update_portfolio(self, portfolio_id: str, portfolio: PortfolioUpdate) -> Optional[PortfolioModel]:
        update_data = portfolio.dict(exclude_unset=True)
        if update_data:
            update_data["updated_at"] = datetime.now()
            result = await self.collection.update_one(
                {"_id": portfolio_id}, {"$set": update_data}
            )
            if result.modified_count:
                return await self.get_portfolio(portfolio_id)
        return None

    async def delete_portfolio(self, portfolio_id: str) -> bool:
        result = await self.collection.delete_one({"_id": portfolio_id})
        return result.deleted_count == 1

    async def list_portfolios(self, skip: int = 0, limit: int = 10) -> List[PortfolioModel]:
        cursor = self.collection.find().skip(skip).limit(limit)
        portfolios = []
        async for document in cursor:
            document["id"] = document.pop("_id")
            portfolios.append(PortfolioModel(**document))
        return portfolios

    async def get_portfolios_by_user(self, user_id: str) -> List[PortfolioModel]:
        cursor = self.collection.find({"user_id": user_id})
        portfolios = []
        async for document in cursor:
            document["id"] = document.pop("_id")
            portfolios.append(PortfolioModel(**document))
        return portfolios

    async def list_all_portfolio_ids(self) -> Optional[List[str]]:
        cursor = self.collection.find({}, {"_id": 1})
        portfolio_ids = []
        async for document in cursor:
            portfolio_ids.append(document["_id"])
        if portfolio_ids:
            return portfolio_ids
        return None
