
from fastapi import Depends, HTTPException, status,Request
from fastapi.security import OAuth2PasswordBearer
from . import token
from jose import JWTError, jwt
import os
from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession
from dotenv import load_dotenv
from src.models import UserModel
from src.database import get_database 
from sqlalchemy.future import select
load_dotenv()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(data: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    return token.verify_token(data, credentials_exception)



async def get_user_id_by_email(email: str,db: AsyncSession = Depends(get_database)):
    """
    Query the database to find the user ID based on the provided email.
    """
    stmt = select(UserModel).where(UserModel.email == email)
    result = await db.execute(stmt)
    user = result.scalars().first()
    return user.user_Id if user else None

async def get_user_id(request: Request, db: AsyncSession = Depends(get_database)):
    """
    Extract the user's email from the JWT token in the Authorization header
    and retrieve the corresponding user ID from the database.
    """
    # Retrieve the Authorization header
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Token is missing or invalid",
        )

    # Extract the token from the header
    token = auth_header[len("Bearer "):]
    if not token:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Token is missing",
        )

    try:
        # Decode the JWT token
        SECRET_KEY = os.getenv("SECRET_KEY")
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        current_user_email = payload.get('sub')
        
        if not current_user_email:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Could not validate credentials",
            )

        # Query the database for the user ID using the email
        user_id = await get_user_id_by_email(current_user_email,db)
        if not user_id:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found",
            )

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Token is invalid or expired",
        )

    return user_id



# Create a CryptContext for bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)