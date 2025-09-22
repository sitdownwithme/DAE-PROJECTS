"""
SQLAlchemy models for ScoutConnect database tables
"""

from sqlalchemy import Column, Integer, String, Date, Text, TIMESTAMP, DECIMAL, ForeignKey, Boolean, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from src.scoutconnect.db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(100), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(20), nullable=False, default='user')  # 'admin', 'coach', 'scout'
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    # Relationships
    evaluations = relationship("Evaluation", back_populates="evaluator")
    watchlists = relationship("Watchlist", back_populates="user")

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    date_of_birth = Column(Date)
    sport = Column(String(50), nullable=False, index=True)
    position = Column(String(50))
    height_cm = Column(Integer)
    weight_kg = Column(Integer)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    # Relationships
    evaluations = relationship("Evaluation", back_populates="player")
    watchlists = relationship("Watchlist", back_populates="player")

class Evaluation(Base):
    __tablename__ = "evaluations"

    id = Column(Integer, primary_key=True, index=True)
    player_id = Column(Integer, ForeignKey("players.id", ondelete="CASCADE"), nullable=False, index=True)
    evaluator_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), index=True)
    sport = Column(String(50), nullable=False)
    criteria = Column(JSON)  # Flexible criteria storage
    score = Column(DECIMAL(5, 2))
    notes = Column(Text)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    # Relationships
    player = relationship("Player", back_populates="evaluations")
    evaluator = relationship("User", back_populates="evaluations")

class Watchlist(Base):
    __tablename__ = "watchlists"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    player_id = Column(Integer, ForeignKey("players.id", ondelete="CASCADE"), nullable=False, index=True)
    notes = Column(Text)
    created_at = Column(TIMESTAMP, server_default=func.now())

    # Relationships
    user = relationship("User", back_populates="watchlists")
    player = relationship("Player", back_populates="watchlists")

    __table_args__ = (
        {'schema': None}
    )