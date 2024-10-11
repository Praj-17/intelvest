# app/routers/users.py

from fastapi import APIRouter, HTTPException, Depends, status
from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from src.schemas import UserCreate, UserOut, UserUpdate
from src.database import get_database
from src.services import UserService

# Authentication dependencies
from src.schemas.user import UserOut as CurrentUser
from src.routes.oauth2 import get_current_user,get_user_id

user_router = APIRouter(
    prefix="/user",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

# Dependency to get the UserService instance
def get_user_service() -> UserService:
    return UserService()

@user_router.post("/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def create_user(
    user: UserCreate,
    db: AsyncSession = Depends(get_database),
    service: UserService = Depends(get_user_service)
):
    # Check if the email is already registered
    existing_user = await service.read_user_from_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = await service.create_user(db, user)
    return UserOut.from_orm(new_user)

@user_router.get("/{user_id}", response_model=UserOut)
async def read_user(
    user_id: int,
    db: AsyncSession = Depends(get_database),
    service: UserService = Depends(get_user_service),
    current_user: CurrentUser = Depends(get_current_user)
    ,current_user_id: str = Depends(get_user_id)
):
    #getting the current user email id
    # print(f"The current user is : {current_user_id}")
    
    user = await service.read_user(db, current_user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    # Optional: Only allow users to read their own data
    # if current_user.user_Id != user_id:
    if current_user_id != user_id:
        raise HTTPException(status_code=403, detail="Not authorized to access this user")
    return UserOut.from_orm(user)

@user_router.put("/{user_id}", response_model=UserOut)
async def update_user(
    user_id: int,
    user_update: UserUpdate,
    db: AsyncSession = Depends(get_database),
    service: UserService = Depends(get_user_service),
    current_user: CurrentUser = Depends(get_current_user)
    ,current_user_id: str = Depends(get_user_id)
):
    
    #getting the current user email id
    # print(f"The current user is : {current_user_email}")

    # Ensure the current_user is allowed to update this user
    if current_user_id != user_id:
        raise HTTPException(status_code=403, detail="Not authorized to update this user")
    updated_user = await service.update_user(db, user_id, user_update)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found or no changes made")
    return UserOut.from_orm(updated_user)

@user_router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user_id: int,
    db: AsyncSession = Depends(get_database),
    service: UserService = Depends(get_user_service),
    current_user: CurrentUser = Depends(get_current_user)
    ,current_user_id: str = Depends(get_user_id)
    
):
    #getting the current user email id
    # print(f"The current user is : {current_user_id}")

    # Ensure the current_user is allowed to delete this user
    if current_user_id != user_id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this user")
    success = await service.delete_user(db, user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return


@user_router.get("/", response_model=List[UserOut])
async def list_users(
    skip: int = 0,
    limit: int = 10,
    db: AsyncSession = Depends(get_database),
    service: UserService = Depends(get_user_service),
    current_user: CurrentUser = Depends(get_current_user)
    ,current_user_id: str = Depends(get_user_id)
):
    
    #getting the current user email id
    print(f"The current user is : {current_user_id}")
    
    # Optional: Restrict this endpoint to admin users
    # if current_user.role_id != admin_role_id:
    #     raise HTTPException(status_code=403, detail="Not authorized to list users")
    users = await service.read_all_users(db, skip=skip, limit=limit)
    return [UserOut.from_orm(user) for user in users]

