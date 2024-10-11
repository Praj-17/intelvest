# app/services/asset_service.py

from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession

from src.CRUD import CRUDAsset
from src.schemas import AssetCreate, AssetUpdate
from src.models import AssetModel
# Assuming AssetUtils is still relevant; otherwise, you can remove it.

class AssetService:
    def __init__(self):
        self.crud = CRUDAsset()

    async def create_asset(self, db: AsyncSession, data: AssetCreate) -> AssetModel:
        return await self.crud.create_asset(db, data)

    async def read_asset(self, db: AsyncSession, p_asset_id: int) -> Optional[AssetModel]:
        return await self.crud.get_asset(db, p_asset_id)

    async def update_asset(self, db: AsyncSession, p_asset_id: int, data: AssetUpdate) -> Optional[AssetModel]:
        return await self.crud.update_asset(db, p_asset_id, data)

    async def delete_asset(self, db: AsyncSession, p_asset_id: int) -> bool:
        return await self.crud.delete_asset(db, p_asset_id)

    async def read_all_assets(self, db: AsyncSession, skip: int = 0, limit: int = 10) -> List[AssetModel]:
        return await self.crud.list_assets(db, skip=skip, limit=limit)

    async def get_assets_by_user(self, db: AsyncSession, user_id: int) -> List[AssetModel]:
        return await self.crud.get_assets_by_user(db, user_id)

    async def get_assets_by_portfolio(self, db: AsyncSession, portfolio_id: int) -> List[AssetModel]:
        return await self.crud.get_assets_by_portfolio(db, portfolio_id)

    async def list_all_asset_ids(self, db: AsyncSession) -> Optional[List[int]]:
        return await self.crud.list_all_asset_ids(db)
