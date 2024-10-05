from fastapi import APIRouter, HTTPException, Depends, status
from typing import List

from src.services import get_portfolio_service, PortfolioService
from src.modules import OkamaReporter
import pandas as pd

analysis_router = APIRouter(
    prefix="/feature/analysis",
    tags=["features"],
    responses={404: {"description": "Not found"}},
)

# Inject OkamaReporter as a dependency for better testability and scalability
def get_okama_reporter() -> OkamaReporter:
    return OkamaReporter()

@analysis_router.get(
    "/",
    response_model=List[str],
    summary="Retrieve all available attributes for analysis",
    status_code=status.HTTP_200_OK
)
async def read_attributes(okama_reporter: OkamaReporter = Depends(get_okama_reporter)) -> List[str]:
    """
    Retrieve a list of all available attributes for analysis.
    """
    return okama_reporter.get_attributes()

@analysis_router.post(
    "/",
    response_model=dict,
    summary="Get analysis data based on portfolio ID and attribute",
    status_code=status.HTTP_200_OK,
    responses={
        404: {"description": "Attribute not found"},
        400: {"description": "Invalid input parameters"},
    }
)
async def get_analysis(
    portfolio_id: str,
    attribute: str,
    service: PortfolioService = Depends(get_portfolio_service),
    okama_reporter: OkamaReporter = Depends(get_okama_reporter)
) -> dict:
    """
    Retrieve analysis data for a given portfolio ID and attribute.
    """
    data = None
    if not portfolio_id or not attribute:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Portfolio ID and attribute are required."
        )

    portfolio = await service.read_portfolio(portfolio_id)
    portfolio = portfolio.to_dict()

    print("________________________________________________________________")
    print(portfolio)
    portfolio['assets']
    processed_portfolio = service.utils.get_all_data(portfolio['assets'])

    print("_______________________________________")
    print(processed_portfolio)
    
    available_attributes = okama_reporter.get_attributes()
    if attribute not in available_attributes:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Attribute '{attribute}' not found. Use GET to retrieve all available attributes."
        )
    
    
    data = okama_reporter.get_an_attribute(processed_portfolio, attribute)
    print("_______________________________________")
    print(data)
    return {"data": data}
