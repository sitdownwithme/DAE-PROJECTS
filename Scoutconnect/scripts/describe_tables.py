"""
Script to generate DESCRIBE documentation for all tables in ScoutConnect database
This creates a text file with table structure information for rubric documentation
"""

import os
import sys
from pathlib import Path

# Add parent directory to path to import database module
sys.path.append(str(Path(__file__).parent.parent))

from database import engine
from sqlalchemy import text

def describe_table(table_name):
    """Get table structure information using SQLite PRAGMA"""
    with engine.connect() as conn:
        result = conn.execute(text(f"PRAGMA table_info({table_name})"))
        columns = result.fetchall()

        if not columns:
            return f"Table '{table_name}' not found or empty."

        output = f"\n=== TABLE: {table_name.upper()} ===\n"
        output += f"{'Column':<20} {'Type':<15} {'Not Null':<10} {'Default':<15} {'Primary Key':<12}\n"
        output += "-" * 75 + "\n"

        for col in columns:
            cid, name, type_, notnull, default, pk = col
            output += f"{name:<20} {type_:<15} {bool(notnull):<10} {str(default):<15} {bool(pk):<12}\n"

        return output

def get_table_list():
    """Get list of all tables in the database"""
    with engine.connect() as conn:
        result = conn.execute(text("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'"))
        return [row[0] for row in result.fetchall()]

def generate_describe_documentation():
    """Generate documentation for all tables"""
    tables = get_table_list()

    documentation = "SCOUTCONNECT DATABASE TABLE STRUCTURES\n"
    documentation += "=" * 50 + "\n"
    documentation += f"Generated using SQLite PRAGMA table_info()\n"
    documentation += f"Found {len(tables)} tables: {', '.join(tables)}\n\n"

    for table in tables:
        documentation += describe_table(table)

    # Save to file
    output_file = Path(__file__).parent / "table_structures_describe.txt"
    with open(output_file, 'w') as f:
        f.write(documentation)

    print(f"Table structure documentation saved to: {output_file}")
    print("\n" + documentation)

if __name__ == "__main__":
    print("Generating DESCRIBE documentation for ScoutConnect tables...")
    generate_describe_documentation()
    print("Documentation generation complete!")