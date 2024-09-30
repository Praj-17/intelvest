from fastapi import APIRouter, HTTPException, Depends, status
from typing import List

from src.schemas import PortfolioCreate, PortfolioOut, PortfolioUpdate
from src.database import get_database
from src.services import PortfolioService

portfolio_router = APIRouter(
    prefix="/portfolio",
    tags=["portfolios"],
    responses={404: {"description": "Not found"}},
)

# Dependency to get the PortfolioService instance
def get_portfolio_service(db=Depends(get_database)) -> PortfolioService:
    return PortfolioService(db)

@portfolio_router.post("/", response_model=PortfolioOut, status_code=status.HTTP_201_CREATED)
async def create_portfolio(portfolio: PortfolioCreate, service: PortfolioService = Depends(get_portfolio_service)):
    new_portfolio = await service.create_portfolio(portfolio)
    return new_portfolio

@portfolio_router.get("/{portfolio_id}", response_model=PortfolioOut)
async def read_portfolio(portfolio_id: str, service: PortfolioService = Depends(get_portfolio_service)):
    portfolio = await service.read_portfolio(portfolio_id)
    if portfolio is None:
        raise HTTPException(status_code=404, detail="Portfolio not found")
    return portfolio

@portfolio_router.put("/{portfolio_id}", response_model=PortfolioOut)
async def update_portfolio(portfolio_id: str, portfolio: PortfolioUpdate, service: PortfolioService = Depends(get_portfolio_service)):
    updated_portfolio = await service.update_portfolio(portfolio_id, portfolio)
    if updated_portfolio is None:
        raise HTTPException(status_code=404, detail="Portfolio not found or no changes made")
    return updated_portfolio

@portfolio_router.delete("/{portfolio_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_portfolio(portfolio_id: str, service: PortfolioService = Depends(get_portfolio_service)):
    success = await service.delete_portfolio(portfolio_id)
    if not success:
        raise HTTPException(status_code=404, detail="Portfolio not found")
    return

@portfolio_router.get("/", response_model=List[PortfolioOut])
async def list_portfolios(skip: int = 0, limit: int = 10, service: PortfolioService = Depends(get_portfolio_service)):
    portfolios = await service.read_all_portfolios(skip=skip, limit=limit)
    return portfolios

@portfolio_router.get("/user/{user_id}", response_model=List[PortfolioOut])
async def get_portfolios_by_user(user_id: str, service: PortfolioService = Depends(get_portfolio_service)):
    portfolios = await service.get_portfolios_by_user(user_id)
    if not portfolios:
        raise HTTPException(status_code=404, detail="No portfolios found for this user")
    return portfolios
