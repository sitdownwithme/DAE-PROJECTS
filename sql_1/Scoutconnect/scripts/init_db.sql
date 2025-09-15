-- ScoutConnect Database Initialization Script
-- Run this script to set up the initial database schema

-- Create database (run as superuser)
-- CREATE DATABASE scoutconnect;
-- CREATE USER scoutconnect_user WITH PASSWORD 'your_password_here';
-- GRANT ALL PRIVILEGES ON DATABASE scoutconnect TO scoutconnect_user;

-- Connect to scoutconnect database and run the following:

-- Users table for authentication
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(20) NOT NULL DEFAULT 'user', -- 'admin', 'coach', 'scout'
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Players table
CREATE TABLE players (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE,
    sport VARCHAR(50) NOT NULL,
    position VARCHAR(50),
    height_cm INTEGER,
    weight_kg INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Evaluations table
CREATE TABLE evaluations (
    id SERIAL PRIMARY KEY,
    player_id INTEGER REFERENCES players(id) ON DELETE CASCADE,
    evaluator_id INTEGER REFERENCES users(id) ON DELETE SET NULL,
    sport VARCHAR(50) NOT NULL,
    criteria JSONB, -- Flexible criteria storage
    score DECIMAL(5,2),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Watchlists table
CREATE TABLE watchlists (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    player_id INTEGER REFERENCES players(id) ON DELETE CASCADE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id, player_id)
);

-- Indexes for performance
CREATE INDEX idx_players_sport ON players(sport);
CREATE INDEX idx_evaluations_player_id ON evaluations(player_id);
CREATE INDEX idx_evaluations_evaluator_id ON evaluations(evaluator_id);
CREATE INDEX idx_watchlists_user_id ON watchlists(user_id);

-- Insert sample data (optional)
-- INSERT INTO users (username, email, password_hash, role) VALUES ('admin', 'admin@scoutconnect.com', 'hashed_password', 'admin');