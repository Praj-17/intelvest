# app/routers/users.py
from fastapi import APIRouter, HTTPException, Depends, status
from typing import List

from src.schemas import UserCreate, UserOut, UserUpdate
from src.database import get_database
from src.services import UserService
from src.routes.authentication import get_user_email

from src.schemas import user
from src.routes import oauth2
# ,current_user: user.Login = Depends(oauth2.get_current_user)
# ,current_user_email: str = Depends(get_user_email)


user_router = APIRouter(
    prefix="/user",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

# Dependency to get the UserService instance
def get_user_service(db=Depends(get_database)) -> UserService:
    return UserService(db)

@user_router.post("/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, service: UserService = Depends(get_user_service)):
    
    #checking if email already exist
    db=get_database()
    existing_user = await db["users"].find_one({"email": user.email}) 
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )
    
    new_user = await service.create_user(user)
    return new_user

@user_router.get("/{user_id}", response_model=UserOut)
async def read_user(user_id: str, service: UserService = Depends(get_user_service),current_user: user.Login = Depends(oauth2.get_current_user),current_user_email: str = Depends(get_user_email)):
    # print("current user email is : " ,current_user_email)
    user = await service.read_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@user_router.put("/{user_id}", response_model=UserOut)
async def update_user(user_id: str, user: UserUpdate, service: UserService = Depends(get_user_service),current_user: user.Login = Depends(oauth2.get_current_user),current_user_email: str = Depends(get_user_email)):
    # print("current user email is : " ,current_user_email)
    updated_user = await service.update_user(user_id, user)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found or no changes made")
    return updated_user

@user_router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: str, service: UserService = Depends(get_user_service),current_user: user.Login = Depends(oauth2.get_current_user),current_user_email: str = Depends(get_user_email)):
    # print("current user email is : " ,current_user_email)
    success = await service.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return


@user_router.get("/", response_model=List[UserOut])
async def list_users(skip: int = 0, limit: int = 10, service: UserService = Depends(get_user_service),current_user: user.Login = Depends(oauth2.get_current_user) ,current_user_email: str = Depends(get_user_email)):
    # print("current user email is : " ,current_user_email)
    users = await service.read_all_users(skip=skip, limit=limit)
    return users
