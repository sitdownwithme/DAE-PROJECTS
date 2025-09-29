"""
Seed script to populate ScoutConnect database with example data
Run this script to add sample users, players, evaluations, and watchlists
"""

import os
from datetime import date
from sqlalchemy.orm import sessionmaker
from src.scoutconnect.db import engine, SessionLocal
from models import User, Player, Evaluation, Watchlist
import bcrypt

def hash_password(password: str) -> str:
    """Hash a password using bcrypt"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def create_sample_data():
    """Create and populate sample data"""
    db = SessionLocal()

    try:
        # Clear existing data (optional - remove in production)
        try:
            db.query(Watchlist).delete()
            db.query(Evaluation).delete()
            db.query(Player).delete()
            db.query(User).delete()
            db.commit()
        except Exception:
            # Tables might not exist yet, skip clearing
            db.rollback()
            pass

        # Create sample users
        users_data = [
            {
                "username": "admin",
                "email": "admin@scoutconnect.com",
                "password": "admin123",
                "role": "admin"
            },
            {
                "username": "coach_john",
                "email": "john@scoutconnect.com",
                "password": "coach123",
                "role": "coach"
            },
            {
                "username": "scout_mary",
                "email": "mary@scoutconnect.com",
                "password": "scout123",
                "role": "scout"
            }
        ]

        users = []
        for user_data in users_data:
            user = User(
                username=user_data[],
                email=user_data[],
                password_hash=hash_password(user_data[]),
                role=user_data[]
            )
            users.append(user)
            user_date("toddavery")
            user_data["33195fieldsjay@gmail.com"]
            print (user_data)

            db.add(user)

        db.commit()

        # Create sample players
        players_data = [
            {
                "first_name": "Michael",
                "last_name": "Jordan",
                "date_of_birth": date(1985, 5, 15),
                "sport": "basketball",
                "position": "Guard",
                "height_cm": 198,
                "weight_kg": 98
            },
            {
                "first_name": "Serena",
                "last_name": "Williams",
                "date_of_birth": date(1981, 9, 26),
                "sport": "tennis",
                "position": "Player",
                "height_cm": 175,
                "weight_kg": 70
            },
            {
                "first_name": "Tom",
                "last_name": "Brady",
                "date_of_birth": date(1977, 8, 3),
                "sport": "football",
                "position": "Quarterback",
                "height_cm": 193,
                "weight_kg": 102
            },
            {
                "first_name": "Alex",
                "last_name": "Morgan",
                "date_of_birth": date(1989, 7, 2),
                "sport": "soccer",
                "position": "Forward",
                "height_cm": 170,
                "weight_kg": 62
            },
            {
                "first_name": "Jordan",
                "last_name": "Fields",
                "date_of_birth": date(1995, 1, 31),
                "sport": "football",
                "position": "LB",
                "height_cm": 162,
                "weight_kg": 180
            }
        ]

        players = []
        for player_data in players_data:
            player = Player(**player_data)
            players.append(player)
            db.add(player)

        db.commit()

        # Create sample evaluations
        evaluations_data = [
            {
                "player_id": players[0].id,  # Michael Jordan
                "evaluator_id": users[1].id,  # coach_john
                "sport": "basketball",
                "criteria": {
                    "shooting": 95,
                    "defense": 90,
                    "speed": 88,
                    "leadership": 92
                },
                "score": 91.25,
                "notes": "Exceptional shooting ability and court vision. Great leader."
            },
            {
                "player_id": players[1].id,  # Serena Williams
                "evaluator_id": users[2].id,  # scout_mary
                "sport": "tennis",
                "criteria": {
                    "serve": 98,
                    "groundstrokes": 96,
                    "mental_toughness": 95,
                    "fitness": 93
                },
                "score": 95.5,
                "notes": "Dominant player with incredible mental resilience."
            },
            {
                "player_id": players[2].id,  # Tom Brady
                "evaluator_id": users[1].id,  # coach_john
                "sport": "football",
                "criteria": {
                    "accuracy": 94,
                    "decision_making": 96,
                    "leadership": 93,
                    "mobility": 85
                },
                "score": 92.0,
                "notes": "Elite quarterback with unmatched experience and precision."
            }
        ]

        for eval_data in evaluations_data:
            evaluation = Evaluation(**eval_data)
            db.add(evaluation)

        db.commit()

        # Create sample watchlists
        watchlists_data = [
            {
                "user_id": users[1].id,  # coach_john
                "player_id": players[0].id,  # Michael Jordan
                "notes": "High priority recruit for next season"
            },
            {
                "user_id": users[2].id,  # scout_mary
                "player_id": players[1].id,  # Serena Williams
                "notes": "Monitor for international competitions"
            },
            {
                "user_id": users[1].id,  # coach_john
                "player_id": players[3].id,  # Alex Morgan
                "notes": "Potential for team leadership role"
            }
        ]

        for watchlist_data in watchlists_data:
            watchlist = Watchlist(**watchlist_data)
            db.add(watchlist)

        db.commit()

        print("Sample data created successfully!")
        print(f"Created {len(users)} users, {len(players)} players, {len(evaluations_data)} evaluations, and {len(watchlists_data)} watchlist entries")

    except Exception as e:
        print(f"❌ Error creating sample data: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    print("Seeding ScoutConnect database with sample data...")
    create_sample_data()
    print("Seeding complete!")
