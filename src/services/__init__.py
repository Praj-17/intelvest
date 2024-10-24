from .user import UserService
from .portfolio import PortfolioService
from fastapi import APIRouter, HTTPException, Depends
from src.database import get_database
from .asset import AssetService
# Dependency to get the PortfolioService instance
def get_portfolio_service(db=Depends(get_database)) -> PortfolioService:
    return PortfolioService()
def get_asset_service(db=Depends(get_database)) -> AssetService:
    return AssetService()

# def get_user_service(db=Depends(get_database)) -> UserService:
#     return UserService()