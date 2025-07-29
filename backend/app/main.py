# app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.note_routes import router as note_router

app = FastAPI(title="Notes API", version="1.0.0")

# Optional: Enable CORS (needed if using frontend like React, etc.)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change this to your frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(note_router)
