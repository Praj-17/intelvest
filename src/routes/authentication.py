#---ak---
from fastapi import APIRouter, status, HTTPException, Depends,Request
from src.schemas import user
from src.database import get_database
from passlib.context import CryptContext
from typing import Optional, Dict 
from src.routes import token,oauth2
from fastapi.security import OAuth2PasswordRequestForm
from jose import JWTError, jwt
from dotenv import load_dotenv
load_dotenv()
import os

auth_router = APIRouter(
    tags=["Authentication"]
)

@auth_router.post('/login')
async def login(request: OAuth2PasswordRequestForm = Depends(), db=Depends(get_database)):
    users_collection = db['users'] 
    usern = await users_collection.find_one({"email": request.username})
    if not usern:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    
    if(request.password!=usern['password']):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect password")
    
    access_token = token.create_access_token(data={"sub": usern['email']})
    return {"access_token": access_token, "token_type": "bearer"}

def get_user_email(request: Request, db=Depends(get_database)):
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Token is missing or invalid",
        )
    
    token = auth_header[len("Bearer "):]
    if not token:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Token is missing",
        )

    try:
    
        ALGORITHM = "HS256"
        SECRET_KEY=os.getenv("SECRET_KEY")
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        current_user_email = payload.get('sub') 

        if not current_user_email:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Could not validate credentials",
            )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Token is invalid or expired",
        )

    return current_user_email
