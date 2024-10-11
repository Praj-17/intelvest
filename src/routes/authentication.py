# app/routers/auth.py

from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.security import OAuth2PasswordRequestForm

from src.schemas import UserOut
from src.database import get_database
from src.services import UserService
from src.routes.token import create_access_token


auth_router = APIRouter(
    tags=["Authentication"]
)


@auth_router.post('/login')
async def login(
    request: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_database),
    service: UserService = Depends(UserService)
):
    # Retrieve the user by email (username)
    usern = await service.read_user_from_email(db, request.username)
    if not usern:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    # Verify the provided password against the stored hashed password
    if not request.password == usern.password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password")
    
    # Create an access token
    access_token = create_access_token(data={"sub": usern.email})
    return {"access_token": access_token, "token_type": "bearer"}
