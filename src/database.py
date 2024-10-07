

# app/database.py
import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
DATABASE_NAME = os.getenv("DATABASE_NAME", "test")

client = AsyncIOMotorClient(MONGODB_URI)
db = client[DATABASE_NAME]

def get_database():
    return db
