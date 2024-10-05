from .user import UserService
from .portfolio import PortfolioService
from fastapi import APIRouter, HTTPException, Depends
from src.database import get_database
# Dependency to get the PortfolioService instance
def get_portfolio_service(db=Depends(get_database)) -> PortfolioService:
    return PortfolioService(db)