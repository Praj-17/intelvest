# app/main.py
from fastapi import FastAPI


from src.routes import user_router, portfolio_router, analysis_router, auth_router
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="Intelvest",
    description="Server for Intelvest",
    version="1.0.0",
)

# ---ak---
@app.get("/")
def home():
    return "hello"

app.include_router(analysis_router)
# ----------------------------

app.include_router(user_router)
app.include_router(portfolio_router)
app.include_router(analysis_router)
app.include_router(auth_router)

# Mount static directory for serving CSS, JS, and images
app.mount("/assets", StaticFiles(directory="src/assets"), name="assets")
# Set up Jinja2Templates to render HTML templates
templates = Jinja2Templates(directory=r"src\assets")
# Serve the homepage
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("home_page.html", {"request": request})
