# app/services/users.py

from typing import Optional, List
from motor.motor_asyncio import AsyncIOMotorDatabase

from src.CRUD import CRUDUser
from src.schemas import UserCreate, UserUpdate
from src.models import UserModel

class UserService:
    def __init__(self, db: AsyncIOMotorDatabase):
        self.crud = CRUDUser(db.users)

    async def create_user(self, data: UserCreate) -> UserModel:
        return await self.crud.create_user(data)

    async def read_user(self, user_id: str) -> Optional[UserModel]:
        return await self.crud.get_user(user_id)

    async def update_user(self, user_id: str, data: UserUpdate) -> Optional[UserModel]:
        return await self.crud.update_user(user_id, data)

    async def delete_user(self, user_id: str) -> bool:
        return await self.crud.delete_user(user_id)

    async def read_all_users(self, skip: int = 0, limit: int = 10) -> List[UserModel]:
        return await self.crud.list_users(skip=skip, limit=limit)

    async def get_user_id_from_email(self, email: str) -> Optional[str]:
        user = await self.crud.read_user_from_email(email)
        if user:
            return str(user.id)
        return None

    async def list_all_user_ids(self) -> Optional[List[str]]:
        user_ids = await self.crud.list_all_user_ids()
        if user_ids:
            return [str(user_id) for user_id in user_ids]
        return None

    async def read_user_from_email(self, email: str) -> Optional[UserModel]:
        return await self.crud.read_user_from_email(email)

    async def read_user_from_number(self, number: str) -> Optional[UserModel]:
        return await self.crud.read_user_from_number(number)
