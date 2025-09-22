# ScoutConnect - Smart Scouting Platform

A backend system designed to help coaches and scouts discover and evaluate under-the-radar athletes. The platform centralizes player data, provides intelligent evaluation tools, and fosters collaboration between sports professionals.

## Features

- **User Authentication**: JWT-based authentication with role-based access control
- **Player Profiles**: Comprehensive athlete profiles with performance metrics
- **Intelligent Scoring**: Universal and sport-specific evaluation criteria
- **Recruitability Analysis**: Hidden talent identification algorithms
- **Collaboration Tools**: Watchlists, comments, and evaluation sharing
- **Data Ingestion**: CSV/JSON import for performance data
- **Injury Tracking**: Risk assessment and recovery monitoring

## Tech Stack

- **Language**: Python 3.13
- **Framework**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Containerization**: Docker & Docker Compose
- **Testing**: pytest
- **Documentation**: OpenAPI/Swagger

## Quick Start

### Prerequisites

- Python 3.13+
- Docker & Docker Compose
- PostgreSQL (optional, can use Docker)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/sitdownwithme/scoutconnect-sqlite.git
   cd scoutconnect-sqlite
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv venv
   # On Windows
   call venv\Scripts\activate
   # On Unix/Mac
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment configuration**
   ```bash
   cp .env.example .env
   # Edit .env with your database credentials
   ```

5. **Run with Docker (Recommended)**
   ```bash
   docker-compose up --build
   ```

6. **Or run locally**
   ```bash
   # Start PostgreSQL first
   # Then run the app
   uvicorn src.scoutconnect.main:app --reload
   ```

### Database Setup

1. **Using Docker Compose** (automatic)
   ```bash
   docker-compose up db
   ```

2. **Manual PostgreSQL setup**
   ```sql
   CREATE DATABASE scoutconnect;
   CREATE USER scoutconnect_user WITH PASSWORD 'your_password';
   GRANT ALL PRIVILEGES ON DATABASE scoutconnect TO scoutconnect_user;
   ```

3. **Run database migrations**
   ```bash
   # The init script runs automatically with Docker
   # For manual setup, run:
   psql -U scoutconnect_user -d scoutconnect -f scripts/init_db.sql
   ```

## API Documentation

Once the application is running, visit:
- **API Docs**: http://localhost:8000/docs
- **Alternative Docs**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health

## Development

### Running Tests
```bash
pytest tests/ -v
```

### Code Formatting
```bash
# Add your preferred formatter (black, isort, etc.)
```

### Database Management
```bash
# Connect to database
psql -U scoutconnect_user -d scoutconnect
```

## Project Structure

```
scoutconnect-sqlite/
├── src/
│   └── scoutconnect/
│       ├── __init__.py
│       ├── main.py          # FastAPI application
│       └── database.py      # Database configuration
├── tests/
│   ├── __init__.py
│   └── test_main.py         # Basic tests
├── scripts/
│   └── init_db.sql          # Database schema
├── docs/                    # Documentation
├── .env                     # Environment variables
├── .gitignore
├── .dockerignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## Environment Variables

Create a `.env` file with:

```env
DATABASE_URL=postgresql://scoutconnect_user:password@localhost:5432/scoutconnect
SECRET_KEY=your-secret-key-here
JWT_SECRET_KEY=your-jwt-secret-key
DEBUG=True
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Roadmap

- Week 2: Database schema completion and authentication
- Week 3: Core API endpoints for players and evaluations
- Week 4: Multi-sport criteria system
- Week 5: Scoring engine implementation
- Week 6+: Collaboration features and advanced analytics

For detailed timeline, see `timeline.md`.
