# app/main.py
from fastapi import FastAPI
from src.routes import user_router

app = FastAPI(
    title="Intelvest",
    description="Server for Intelvest",
    version="1.0.0",
)

app.include_router(user_router)
