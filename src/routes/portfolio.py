# app/routes/portfolio_router.py

from fastapi import APIRouter, UploadFile, File, HTTPException, status, Depends
from typing import List, Optional
import pandas as pd
from io import StringIO
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.models import AssetType, UserModel
from src.schemas import (
    PortfolioCreate, PortfolioOut, PortfolioUpdate, 
    AssetCreate, AssetOut
)
from src.services import PortfolioService, AssetService
from src.database import get_database
from src.utils import get_current_user,get_user_id
from src.services import get_asset_service, get_portfolio_service


portfolio_router = APIRouter(
    prefix="/portfolio",
    tags=["portfolios"],
    responses={404: {"description": "Not found"}},
)


@portfolio_router.post("/upload", response_model=PortfolioOut, status_code=status.HTTP_201_CREATED)
async def upload_portfolio(
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_database),
    service: PortfolioService = Depends(get_portfolio_service),
    asset_service: AssetService =  Depends(get_asset_service),
    current_user: UserModel = Depends(get_current_user),
    current_user_id: str = Depends(get_user_id)
):
    required_columns = {'symbol', 'quantity', 'purchase_price', 'purchase_date', 'asset_type'}

    # Process CSV file
    if not file:
        raise HTTPException(
            status_code=400, 
            detail="Please upload a CSV file with the required columns."
        )
    if file.content_type != 'text/csv':
        raise HTTPException(
            status_code=400, 
            detail="Invalid file type. Please upload a CSV file."
        )
    try:
        content = await file.read()
        decoded_content = content.decode('utf-8')
        df = pd.read_csv(StringIO(decoded_content))

        if not required_columns.issubset(df.columns):
            missing = required_columns - set(df.columns)
            raise HTTPException(
                status_code=400, 
                detail=f"Missing columns in CSV: {', '.join(missing)}"
            )
        # Create the portfolio using the service
        portfolio_data = PortfolioCreate(
            portfolio_name="Uploaded Portfolio",
            user_id=current_user_id
        )
        new_portfolio = await service.create_portfolio(db, portfolio_data)

        assets = []
        for _, row in df.iterrows():
            symbol = str(row['symbol']).strip() if pd.notna(row['symbol']) else None
            quantity = int(row['quantity']) if pd.notna(row['quantity']) else 0
            purchase_price = str(row['purchase_price']) if pd.notna(row['purchase_price']) else None
            purchase_date_str = str(row['purchase_date']).strip() if pd.notna(row['purchase_date']) else None
            purchase_date = datetime.strptime(purchase_date_str, '%d-%m-%Y').date() if purchase_date_str else None
            asset_type = str(row['asset_type']).strip()

            # Validate asset_type
            try:
                asset_type_enum = AssetType(asset_type)
            except ValueError:
                raise HTTPException(
                    status_code=400, 
                    detail=f"Invalid asset type: {asset_type}"
                )

            if not symbol or not purchase_date or not asset_type_enum:
                continue  # Skip invalid rows

            asset = AssetCreate(
                asset_type=asset_type_enum,
                symbol=symbol,
                purchase_date=purchase_date,
                quantity=quantity,
                purchase_price=purchase_price,
                user_id=current_user_id,
                portfolio_id=new_portfolio.p_id
            )
            new_asset = await asset_service.create_asset(db, asset)
            assets.append(new_asset)
            
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(
            status_code=400, 
            detail=f"Error processing the CSV file: {str(e)}"
        )

    # Load the assets into the new_portfolio
    new_portfolio.assets = assets
    return PortfolioOut.from_orm(new_portfolio)

@portfolio_router.post("/", response_model=PortfolioOut, status_code=status.HTTP_201_CREATED)
async def create_portfolio(
    portfolio_data: PortfolioCreate,
    db: AsyncSession = Depends(get_database),
    portfolio_service: PortfolioService = Depends(get_portfolio_service),
    asset_service: AssetService = Depends(get_asset_service),
    current_user: UserModel = Depends(get_current_user)
    ,current_user_id: str = Depends(get_user_id)
):
    # Assign the authenticated user's ID to the portfolio
    portfolio_data.user_id = current_user_id

    # Create the portfolio using the service
    new_portfolio = await portfolio_service.create_portfolio(db, portfolio_data)

    assets = []
    
    if portfolio_data.assets:
        for asset_data in portfolio_data.assets:
            asset_data.user_id = current_user_id
            asset_data.portfolio_id = new_portfolio.p_id
            new_asset = await asset_service.create_asset(db, asset_data)
            assets.append(new_asset)

    # Load the assets into the new_portfolio
    new_portfolio.assets = assets

    return PortfolioOut.from_orm(new_portfolio)

@portfolio_router.put("/{portfolio_id}", response_model=PortfolioOut)
async def update_portfolio(
    portfolio_id: int,
    portfolio_update: PortfolioUpdate,
    db: AsyncSession = Depends(get_database),
    portfolio_service: PortfolioService = Depends(get_portfolio_service),
    asset_service: AssetService = Depends(get_asset_service),
    current_user: UserModel = Depends(get_current_user)
    ,current_user_id: str = Depends(get_user_id)
    
):
    #getting the current user email id
    # print(f"The current user is : {current_user_id}")

    # Retrieve the existing portfolio
    existing_portfolio = await portfolio_service.read_portfolio(db, portfolio_id)
    if existing_portfolio is None or existing_portfolio.user_id != current_user_id:
        raise HTTPException(status_code=404, detail="Portfolio not found")

    # Update the portfolio using the service
    updated_portfolio = await portfolio_service.update_portfolio(db, portfolio_id, portfolio_update)
    if updated_portfolio is None:
        raise HTTPException(status_code=400, detail="No changes made or update failed")

    # Optionally handle assets update here if needed

    # Fetch the updated portfolio with assets
    portfolio_with_assets = await portfolio_service.read_portfolio(db, portfolio_id)

    return PortfolioOut.from_orm(portfolio_with_assets)

@portfolio_router.get("/{portfolio_id}", response_model=PortfolioOut)
async def read_portfolio(
    portfolio_id: int,
    db: AsyncSession = Depends(get_database),
    service: PortfolioService = Depends(get_portfolio_service),
    current_user: UserModel = Depends(get_current_user)
    ,current_user_id: str = Depends(get_user_id)
    
):
    #getting the current user email id
    # print(f"The current user is : {current_user_id}")

    portfolio = await service.read_portfolio(db, portfolio_id)
    if portfolio is None or portfolio.user_id != current_user_id:
        raise HTTPException(status_code=404, detail="Portfolio not found")
    return PortfolioOut.from_orm(portfolio)

@portfolio_router.delete("/{portfolio_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_portfolio(
    portfolio_id: int,
    db: AsyncSession = Depends(get_database),
    service: PortfolioService = Depends(get_portfolio_service),
    current_user: UserModel = Depends(get_current_user)
    ,current_user_id: str = Depends(get_user_id)
    
):
    #getting the current user email id
    # print(f"The current user is : {current_user_id}")

    existing_portfolio = await service.read_portfolio(db, portfolio_id)
    if existing_portfolio is None or existing_portfolio.user_id != current_user_id:
        raise HTTPException(status_code=404, detail="Portfolio not found")

    success = await service.delete_portfolio(db, portfolio_id)
    if not success:
        raise HTTPException(status_code=400, detail="Failed to delete portfolio")
    return

@portfolio_router.get("/", response_model=List[PortfolioOut])
async def list_portfolios(
    skip: int = 0,
    limit: int = 10,
    db: AsyncSession = Depends(get_database),
    service: PortfolioService = Depends(get_portfolio_service),
    current_user: UserModel = Depends(get_current_user)
    ,current_user_id: str = Depends(get_user_id)
    
):
    #getting the current user email id
    # print(f"The current user is : {current_user_id}")

    portfolios = await service.get_portfolios_by_user(db, current_user_id)
    return [PortfolioOut.from_orm(p) for p in portfolios]
