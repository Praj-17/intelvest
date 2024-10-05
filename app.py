# app/main.py
from fastapi import FastAPI
from src.routes import user_router, portfolio_router, analysis_router

app = FastAPI(
    title="Intelvest",
    description="Server for Intelvest",
    version="1.0.0",
)

app.include_router(user_router)
app.include_router(portfolio_router)
app.include_router(analysis_router)