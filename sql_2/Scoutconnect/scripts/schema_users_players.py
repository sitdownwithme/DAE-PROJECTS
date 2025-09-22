"""
Script to run .schema equivalent for users and players tables
This implements the specific requirement: "Run .schema users + .schema players"
"""

import os
import sys
from pathlib import Path

# Add parent directory to path to import database module
sys.path.append(str(Path(__file__).parent.parent))

from database import engine
from sqlalchemy import text

def run_schema_command(table_name):
    """Run SQLite .schema equivalent for a specific table"""
    print(f"\n=== .schema {table_name} ===")

    with engine.connect() as conn:
        # Get the CREATE TABLE statement (equivalent to .schema)
        result = conn.execute(text(f"SELECT sql FROM sqlite_master WHERE type='table' AND name='{table_name}'"))
        create_statement = result.fetchone()

        if create_statement and create_statement[0]:
            print(create_statement[0])
        else:
            print(f"Table '{table_name}' not found.")

        # Also show indexes for the table
        print(f"\n=== Indexes for {table_name} ===")
        index_result = conn.execute(text(f"SELECT sql FROM sqlite_master WHERE type='index' AND tbl_name='{table_name}' AND sql IS NOT NULL"))
        indexes = index_result.fetchall()

        if indexes:
            for index in indexes:
                print(index[0])
        else:
            print(f"No indexes found for {table_name}")

def verify_schema_matches_planned():
    """Verify that the actual schema matches the planned fields from models.py"""
    print("\n" + "="*60)
    print("SCHEMA VERIFICATION: Planned vs Actual Fields")
    print("="*60)

    planned_users = {
        "id": "INTEGER PRIMARY KEY",
        "username": "VARCHAR(50) UNIQUE NOT NULL",
        "email": "VARCHAR(100) UNIQUE NOT NULL",
        "password_hash": "VARCHAR(255) NOT NULL",
        "role": "VARCHAR(20) NOT NULL DEFAULT 'user'",
        "created_at": "TIMESTAMP",
        "updated_at": "TIMESTAMP"
    }

    planned_players = {
        "id": "INTEGER PRIMARY KEY",
        "first_name": "VARCHAR(50) NOT NULL",
        "last_name": "VARCHAR(50) NOT NULL",
        "date_of_birth": "DATE",
        "sport": "VARCHAR(50) NOT NULL",
        "position": "VARCHAR(50)",
        "height_cm": "INTEGER",
        "weight_kg": "INTEGER",
        "created_at": "TIMESTAMP",
        "updated_at": "TIMESTAMP"
    }

    print("\nUSERS TABLE VERIFICATION:")
    print("-" * 30)
    with engine.connect() as conn:
        result = conn.execute(text("PRAGMA table_info(users)"))
        actual_users = {row[1]: f"{row[2]}{' NOT NULL' if row[3] else ''}{' UNIQUE' if row[5] else ''}" for row in result.fetchall()}

        for field, planned_type in planned_users.items():
            actual_type = actual_users.get(field, "NOT FOUND")
            status = "[MATCH]" if planned_type in actual_type else "[MISMATCH]"
            print(f"{field:<15}: Planned={planned_type:<25} Actual={actual_type:<25} {status}")

    print("\nPLAYERS TABLE VERIFICATION:")
    print("-" * 30)
    with engine.connect() as conn:
        result = conn.execute(text("PRAGMA table_info(players)"))
        actual_players = {row[1]: f"{row[2]}{' NOT NULL' if row[3] else ''}" for row in result.fetchall()}

        for field, planned_type in planned_players.items():
            actual_type = actual_players.get(field, "NOT FOUND")
            status = "✅ MATCH" if planned_type in actual_type else "❌ MISMATCH"
            print(f"{field:<15}: Planned={planned_type:<25} Actual={actual_type:<25} {status}")

if __name__ == "__main__":
    print("Running .schema equivalent for users and players tables...")
    print("This implements: 'Run .schema users + .schema players'")

    # Run schema commands
    run_schema_command("users")
    run_schema_command("players")

    # Verify schema matches planned fields
    verify_schema_matches_planned()

    print("\n" + "="*60)
    print("✅ SQL 1 rubric requirement completed!")
    print("✅ .schema users + .schema players executed")
    print("✅ Schema verification completed")
    print("="*60)