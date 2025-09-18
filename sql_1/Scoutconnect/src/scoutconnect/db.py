from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# Load DB path from environment (.env file)
DB_PATH = os.getenv("DB_PATH", "scoutconnect.db")

# Create SQLite engine
engine = create_engine(f"sqlite:///{DB_PATH}", echo=True)

# Session maker for database connections
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()
