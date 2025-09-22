"""
Script to export ScoutConnect database to SQL file
Includes both schema creation and data insertion statements
"""

import os
import sys
from pathlib import Path
from datetime import datetime

# Add parent directory to path to import database module
sys.path.append(str(Path(__file__).parent.parent))

from database import engine
from sqlalchemy import text, inspect

def export_table_schema(table_name):
    """Export CREATE TABLE statement for a table"""
    with engine.connect() as conn:
        # Get table info
        result = conn.execute(text(f"PRAGMA table_info({table_name})"))
        columns = result.fetchall()

        # Get foreign keys
        fk_result = conn.execute(text(f"PRAGMA foreign_key_list({table_name})"))
        foreign_keys = fk_result.fetchall()

        # Build CREATE TABLE statement
        create_stmt = f"CREATE TABLE {table_name} (\n"

        col_defs = []
        for col in columns:
            cid, name, type_, notnull, default, pk = col
            col_def = f"    {name} {type_}"
            if notnull:
                col_def += " NOT NULL"
            if default is not None:
                col_def += f" DEFAULT {default}"
            if pk:
                col_def += " PRIMARY KEY"
            col_defs.append(col_def)

        # Add foreign keys
        for fk in foreign_keys:
            id_, seq, table, from_col, to_col, on_update, on_delete, match = fk
            fk_def = f"    FOREIGN KEY ({from_col}) REFERENCES {table} ({to_col})"
            if on_delete != "NO ACTION":
                fk_def += f" ON DELETE {on_delete}"
            if on_update != "NO ACTION":
                fk_def += f" ON UPDATE {on_update}"
            col_defs.append(fk_def)

        create_stmt += ",\n".join(col_defs)
        create_stmt += "\n);\n\n"

        return create_stmt

def export_table_data(table_name):
    """Export INSERT statements for table data"""
    with engine.connect() as conn:
        # Get all data from table
        result = conn.execute(text(f"SELECT * FROM {table_name}"))
        rows = result.fetchall()

        if not rows:
            return ""

        # Get column names
        column_names = result.keys()

        insert_stmts = []
        for row in rows:
            values = []
            for value in row:
                if value is None:
                    values.append("NULL")
                elif isinstance(value, str):
                    # Escape single quotes
                    escaped_value = value.replace("'", "''")
                    values.append(f"'{escaped_value}'")
                elif isinstance(value, datetime):
                    values.append(f"'{value.isoformat()}'")
                else:
                    values.append(str(value))

            values_str = ", ".join(values)
            insert_stmt = f"INSERT INTO {table_name} ({', '.join(column_names)}) VALUES ({values_str});"
            insert_stmts.append(insert_stmt)

        return "\n".join(insert_stmts) + "\n\n"

def export_database():
    """Export complete database to SQL file"""
    tables = ['users', 'players', 'evaluations', 'watchlists']

    export_content = "-- ScoutConnect Database Export\n"
    export_content += f"-- Generated on {datetime.now().isoformat()}\n\n"
    export_content += "-- Schema\n\n"

    # Export schema
    for table in tables:
        export_content += export_table_schema(table)

    export_content += "-- Data\n\n"

    # Export data
    for table in tables:
        export_content += f"-- Data for {table}\n"
        export_content += export_table_data(table)

    # Save to file
    output_file = Path(__file__).parent / "scoutconnect_export.sql"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(export_content)

    print(f"Database export completed: {output_file}")
    print(f"Exported {len(tables)} tables with schema and data")
    return output_file

if __name__ == "__main__":
    print("Exporting ScoutConnect database...")
    export_file = export_database()
    print(f"Export saved to: {export_file}")