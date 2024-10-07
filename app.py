# app/main.py
from fastapi import FastAPI
from src.routes import user_router, portfolio_router

# ---ak---
from src.routes import authentication
from src import databaseSQL
from src.models import portfolio_sql
# --------

app = FastAPI(
    title="Intelvest",
    description="Server for Intelvest",
    version="1.0.0",
)

# ---ak---
@app.get("/")
def home():
    return "hello"

portfolio_sql.Base.metadata.create_all(databaseSQL.engine)

app.include_router(authentication.router)
# ----------------------------

app.include_router(user_router)
app.include_router(portfolio_router)
