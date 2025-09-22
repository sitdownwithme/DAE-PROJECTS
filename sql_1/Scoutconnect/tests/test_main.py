"""
Tests for ScoutConnect main application
"""

from fastapi.testclient import TestClient
from scoutconnect.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to ScoutConnect API"}

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}