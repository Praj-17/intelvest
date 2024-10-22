# app/crud_user.py

from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from datetime import datetime

from src.models import UserModel
from src.schemas import UserCreate, UserUpdate
from src.utils import get_password_hash
class CRUDUser:
    def __init__(self):
        pass  # No initialization needed

    async def create_user(self, db: AsyncSession, user: UserCreate) -> UserModel:
        # Hash the password before storing it
        user_data = user.dict(exclude={'password'})
        user_data['password'] =  get_password_hash(user.password)
        user_data['added_on'] = datetime.now()

        new_user = UserModel(**user_data)
        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)
        return new_user

    async def get_user(self, db: AsyncSession, user_id: int) -> Optional[UserModel]:
        result = await db.execute(
            select(UserModel).where(UserModel.user_Id == user_id)
        )
        user = result.scalar_one_or_none()
        return user

    async def update_user(self, db: AsyncSession, user_id: int, user: UserUpdate) -> Optional[UserModel]:
        result = await db.execute(
            select(UserModel).where(UserModel.user_Id == user_id)
        )
        existing_user = result.scalar_one_or_none()
        if not existing_user:
            return None

        update_data = user.dict(exclude_unset=True)
        if 'password' in update_data:
            # Hash the new password before updating
            update_data['password'] = get_password_hash(update_data['password'])
        update_data['updated_at'] = datetime.utcnow()

        for key, value in update_data.items():
            setattr(existing_user, key, value)

        await db.commit()
        await db.refresh(existing_user)
        return existing_user

    async def delete_user(self, db: AsyncSession, user_id: int) -> bool:
        result = await db.execute(
            select(UserModel).where(UserModel.user_Id == user_id)
        )
        user = result.scalar_one_or_none()
        if not user:
            return False

        await db.delete(user)
        await db.commit()
        return True

    async def list_users(self, db: AsyncSession, skip: int = 0, limit: int = 10) -> List[UserModel]:
        result = await db.execute(
            select(UserModel).offset(skip).limit(limit)
        )
        users = result.scalars().all()
        return users

    async def read_user_from_email(self, db: AsyncSession, email: str) -> Optional[UserModel]:
        result = await db.execute(
            select(UserModel).where(UserModel.email == email)
        )
        user = result.scalar_one_or_none()
        return user

    async def read_user_from_number(self, db: AsyncSession, phone: str) -> Optional[UserModel]:
        result = await db.execute(
            select(UserModel).where(UserModel.phone == phone)
        )
        user = result.scalar_one_or_none()
        return user

    async def list_all_user_ids(self, db: AsyncSession) -> Optional[List[int]]:
        result = await db.execute(select(UserModel.user_Id))
        user_ids = result.scalars().all()
        if user_ids:
            return user_ids
        return None
