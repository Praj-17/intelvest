# app/services/user_service.py

from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession

from src.CRUD import CRUDUser
from src.schemas import UserCreate, UserUpdate
from src.models import UserModel

class UserService:
    def __init__(self):
        self.crud = CRUDUser()

    async def create_user(self, db: AsyncSession, data: UserCreate) -> UserModel:
        return await self.crud.create_user(db, data)

    async def read_user(self, db: AsyncSession, user_id: int) -> Optional[UserModel]:
        return await self.crud.get_user(db, user_id)

    async def update_user(self, db: AsyncSession, user_id: int, data: UserUpdate) -> Optional[UserModel]:
        return await self.crud.update_user(db, user_id, data)

    async def delete_user(self, db: AsyncSession, user_id: int) -> bool:
        return await self.crud.delete_user(db, user_id)

    async def read_all_users(self, db: AsyncSession, skip: int = 0, limit: int = 10) -> List[UserModel]:
        return await self.crud.list_users(db, skip=skip, limit=limit)

    async def get_user_id_from_email(self, db: AsyncSession, email: str) -> Optional[int]:
        user = await self.crud.read_user_from_email(db, email)
        if user:
            return user.user_Id
        return None

    async def list_all_user_ids(self, db: AsyncSession) -> Optional[List[int]]:
        user_ids = await self.crud.list_all_user_ids(db)
        if user_ids:
            return user_ids
        return None

    async def read_user_from_email(self, db: AsyncSession, email: str) -> Optional[UserModel]:
        return await self.crud.read_user_from_email(db, email)

    async def read_user_from_number(self, db: AsyncSession, phone: str) -> Optional[UserModel]:
        return await self.crud.read_user_from_number(db, phone)
