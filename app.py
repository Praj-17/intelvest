# app/main.py
from fastapi import FastAPI
from src.routes import user_router, portfolio_router
# ---ak---
from src.routes import authentication
# --------
app = FastAPI(
    title="Intelvest",
    description="Server for Intelvest",
    version="1.0.0",
)
# ---ak---
@app.get("/")
def pr():
    return "hello"

app.include_router(authentication.router)
# ----------------------------

app.include_router(user_router)
app.include_router(portfolio_router)
