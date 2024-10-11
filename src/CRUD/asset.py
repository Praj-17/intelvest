# app/crud_asset.py

from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from datetime import datetime, date

from src.schemas import AssetCreate, AssetUpdate
from src.models import AssetModel
from sqlalchemy.exc import NoResultFound

class CRUDAsset:
    def __init__(self):
        pass  # No initialization needed

    async def create_asset(self, db: AsyncSession, asset: AssetCreate) -> AssetModel:
        new_asset = AssetModel(
            user_id=asset.user_id,
            portfolio_id=asset.portfolio_id,
            asset_type=asset.asset_type,
            symbol=asset.symbol,
            purchase_date=asset.purchase_date,
            quantity=asset.quantity,
            purchase_price=asset.purchase_price,
            added_on=date.today(),
            asset_id=asset.asset_id or 0  # Use provided asset_id or default to 0
        )
        db.add(new_asset)
        await db.commit()
        await db.refresh(new_asset)
        return new_asset

    async def get_asset(self, db: AsyncSession, p_asset_id: int) -> Optional[AssetModel]:
        result = await db.execute(
            select(AssetModel).where(AssetModel.p_asset_id == p_asset_id)
        )
        asset = result.scalar_one_or_none()
        return asset

    async def update_asset(self, db: AsyncSession, p_asset_id: int, asset_update: AssetUpdate) -> Optional[AssetModel]:
        result = await db.execute(
            select(AssetModel).where(AssetModel.p_asset_id == p_asset_id)
        )
        existing_asset = result.scalar_one_or_none()
        if not existing_asset:
            return None

        update_data = asset_update.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(existing_asset, key, value)
        await db.commit()
        await db.refresh(existing_asset)
        return existing_asset

    async def delete_asset(self, db: AsyncSession, p_asset_id: int) -> bool:
        result = await db.execute(
            select(AssetModel).where(AssetModel.p_asset_id == p_asset_id)
        )
        asset = result.scalar_one_or_none()
        if not asset:
            return False
        await db.delete(asset)
        await db.commit()
        return True

    async def list_assets(self, db: AsyncSession, skip: int = 0, limit: int = 10) -> List[AssetModel]:
        result = await db.execute(
            select(AssetModel).offset(skip).limit(limit)
        )
        assets = result.scalars().all()
        return assets

    async def get_assets_by_user(self, db: AsyncSession, user_id: int) -> List[AssetModel]:
        result = await db.execute(
            select(AssetModel).where(AssetModel.user_id == user_id)
        )
        assets = result.scalars().all()
        return assets

    async def get_assets_by_portfolio(self, db: AsyncSession, portfolio_id: int) -> List[AssetModel]:
        result = await db.execute(
            select(AssetModel).where(AssetModel.portfolio_id == portfolio_id)
        )
        assets = result.scalars().all()
        return [asset.to_dict() for asset in assets]

    async def list_all_asset_ids(self, db: AsyncSession) -> Optional[List[int]]:
        result = await db.execute(select(AssetModel.p_asset_id))
        asset_ids = result.scalars().all()
        if asset_ids:
            return asset_ids
        return None
