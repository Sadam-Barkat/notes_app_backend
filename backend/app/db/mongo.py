# app/db/mongo.py

import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get MongoDB URI from .env
MONGODB_URI = os.getenv("MONGODB_URI")

# Connect to MongoDB Atlas
client = AsyncIOMotorClient(MONGODB_URI)
db = client["notes_app_db"]  # database name

# Notes collection
notes_collection = db["notes"]
