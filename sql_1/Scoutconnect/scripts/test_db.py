"""
Test script to check database tables
"""

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from database import engine, create_tables
from sqlalchemy import text
import models  # Ensure models are loaded

def test_db():
    # Create tables first
    create_tables()

    with engine.connect() as conn:
        # List all tables
        result = conn.execute(text("SELECT name FROM sqlite_master WHERE type='table'"))
        tables = result.fetchall()
        print(f"Found tables: {[row[0] for row in tables]}")

        # Try to query users table
        try:
            result = conn.execute(text("SELECT COUNT(*) FROM users"))
            count = result.fetchone()[0]
            print(f"Users table has {count} rows")
        except Exception as e:
            print(f"Error querying users: {e}")

if __name__ == "__main__":
    test_db()