from fastapi import APIRouter, UploadFile, File, HTTPException, status, Depends, Form

from typing import List
import pandas as pd
from io import StringIO
from datetime import datetime
from src.models.portfolio import AssetType
from src.schemas import PortfolioCreate, PortfolioOut, PortfolioUpdate
from src.services import PortfolioService
from src.database import get_database

# ---ak---
from src.schemas import user
from src.routes import oauth2
# ,current_user: user.Login = Depends(oauth2.get_current_user)
# --------

from src.services import get_portfolio_service
from typing import Optional

portfolio_router = APIRouter(
    prefix="/portfolio",
    tags=["portfolios"],
    responses={404: {"description": "Not found"}},
)


# Dependency to get the PortfolioService instance
def get_portfolio_service(db=Depends(get_database),current_user: user.Login = Depends(oauth2.get_current_user)) -> PortfolioService:
    return PortfolioService(db)

@portfolio_router.post("/upload", response_model=PortfolioOut, status_code=status.HTTP_201_CREATED)
async def create_portfolio(
   file: Optional[UploadFile] = File(None),
    service: PortfolioService = Depends(get_portfolio_service)
):
    temp_user_id = "PRAJWAL"

        # Process CSV file
    if file.content_type != 'text/csv':
        raise HTTPException(
            status_code=400, 
            detail="Invalid file type. Please upload a CSV file."
        )
    try:
        content = await file.read()
        decoded_content = content.decode('utf-8')
        df = pd.read_csv(StringIO(decoded_content))

        required_columns = {'symbol', 'quantity', 'purchase_price', 'purchase_date', 'asset_type'}
        if not required_columns.issubset(df.columns):
            missing = required_columns - set(df.columns)
            raise HTTPException(
                status_code=400, 
                detail=f"Missing columns in CSV: {', '.join(missing)}"
            )

        assets = []
        for _, row in df.iterrows():
            symbol = str(row['symbol']).strip().strip('"').strip("'") if pd.notna(row['symbol']) else None
            quantity = float(row['quantity']) if pd.notna(row['quantity']) else 0.0
            purchase_price = float(row['purchase_price']) if pd.notna(row['purchase_price']) else None
            purchase_date_str = str(row['purchase_date']).strip() if pd.notna(row['purchase_date']) else None
            purchase_date = datetime.strptime(purchase_date_str, '%d-%m-%Y') if purchase_date_str else None
            asset_type = str(row['asset_type']).strip()

            # Validate asset_type
            try:
                asset_type_enum = AssetType(asset_type)
            except ValueError:
                raise HTTPException(
                    status_code=400, 
                    detail=f"Invalid asset type: {asset_type}"
                )

            asset = {
                "symbol":symbol,
                "quantity":quantity,
                "purchase_price":purchase_price,
                "purchase_date":purchase_date,
                "asset_type":asset_type_enum
            }
            assets.append(asset)

        portfolio_data = PortfolioCreate(
            user_id=temp_user_id,  # Assign authenticated user ID
            assets=assets
        )



    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(
            status_code=400, 
            detail=f"Error processing the CSV file: {str(e)}"
        )

    # Create the portfolio using the service
    new_portfolio = await service.create_portfolio(portfolio_data)
    return new_portfolio


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
