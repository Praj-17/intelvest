#---ak---
from fastapi import APIRouter, status, HTTPException, Depends
from src.schemas import user
from src.database import get_database
from passlib.context import CryptContext
from typing import Optional, Dict 
from src.routes import token
from fastapi.security import OAuth2PasswordRequestForm

api_router = APIRouter(
    tags=["Authentication"]
)

@api_router.post('/login')
async def login(request: OAuth2PasswordRequestForm = Depends(), db=Depends(get_database)):
    users_collection = db['users'] 
    usern = await users_collection.find_one({"email": request.username})
    # return usern
    # print(usern)
    if not usern:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    
    if(request.password!=usern['password']):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect password")
    
    access_token = token.create_access_token(data={"sub": usern['email']})
    return {"access_token": access_token, "token_type": "bearer"}
