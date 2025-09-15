"""
ScoutConnect - Smart Scouting Platform API
Main FastAPI application entry point
"""

from fastapi import FastAPI

app = FastAPI(
    title="ScoutConnect API",
    description="Smart Scouting Platform for Talent Discovery & Collaboration",
    version="0.1.0"
)

@app.get("/")
async def root():
    return {"message": "Welcome to ScoutConnect API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}