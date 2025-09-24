#!/usr/bin/env python3
"""
Initialize ScoutConnect database with tables
"""

from src.scoutconnect.db import engine, Base
from models import User, Player, Evaluation, Watchlist

def init_database():
    """Create all database tables"""
    print("Creating database tables...")

    # Create all tables defined in the models
    Base.metadata.create_all(bind=engine)

    print("✅ Database tables created successfully!")
    print("Tables created:")
    print("  - users")
    print("  - players")
    print("  - evaluations")
    print("  - watchlists")

if __name__ == "__main__":
    init_database()