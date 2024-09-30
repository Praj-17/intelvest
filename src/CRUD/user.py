# app/crud.py
from typing import List, Optional
from motor.motor_asyncio import AsyncIOMotorCollection
from datetime import datetime
import uuid

from src.schemas import UserCreate, UserUpdate
from src.models import UserModel

class CRUDUser:
    def __init__(self, collection: AsyncIOMotorCollection):
        self.collection = collection

    async def create_user(self, user: UserCreate) -> UserModel:
        user_dict = user.dict()
        user_dict["created_at"] = datetime.now()
        user_dict["updated_at"] = datetime.now()
        user_dict["_id"] = str(uuid.uuid4())
        await self.collection.insert_one(user_dict)
        user_dict["id"] = user_dict.pop("_id")
        return UserModel(**user_dict)

    async def get_user(self, user_id: str) -> Optional[UserModel]:
        document = await self.collection.find_one({"_id": user_id})
        if document:
            document["id"] = document.pop("_id")
            return UserModel(**document)
        return None

    async def update_user(self, user_id: str, user: UserUpdate) -> Optional[UserModel]:
        update_data = user.dict(exclude_unset=True)
        if update_data:
            update_data["updated_at"] = datetime.now()
            result = await self.collection.update_one(
                {"_id": user_id}, {"$set": update_data}
            )
            if result.modified_count:
                return await self.get_user(user_id)
        return None

    async def delete_user(self, user_id: str) -> bool:
        result = await self.collection.delete_one({"_id": user_id})
        return result.deleted_count == 1

    async def list_users(self, skip: int = 0, limit: int = 10) -> List[UserModel]:
        cursor = self.collection.find().skip(skip).limit(limit)
        users = []
        async for document in cursor:
            document["id"] = document.pop("_id")
            users.append(UserModel(**document))
        return users

    async def read_user_from_email(self, email: str) -> Optional[UserModel]:
        document = await self.collection.find_one({"email": email})
        if document:
            document["id"] = document.pop("_id")
            return UserModel(**document)
        return None

    async def read_user_from_number(self, number: str) -> Optional[UserModel]:
        document = await self.collection.find_one({"number": number})
        if document:
            document["id"] = document.pop("_id")
            return UserModel(**document)
        return None

    async def list_all_user_ids(self) -> Optional[List[str]]:
        cursor = self.collection.find({}, {"_id": 1})
        user_ids = []
        async for document in cursor:
            user_ids.append(document["_id"])
        if user_ids:
            return user_ids
        return None
