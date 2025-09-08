# Contributing to ScoutConnect

Welcome to ScoutConnect! We're excited that you're interested in contributing to our smart scouting platform for talent discovery and collaboration. This document provides guidelines and information for contributing to the project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Project Structure](#project-structure)
- [Contributing Process](#contributing-process)
- [Coding Standards](#coding-standards)
- [Testing Guidelines](#testing-guidelines)
- [Documentation](#documentation)
- [Issue Guidelines](#issue-guidelines)
- [Pull Request Process](#pull-request-process)
- [Release Process](#release-process)

## Code of Conduct

This project adheres to a code of conduct that we expect all contributors to follow. Please be respectful, inclusive, and professional in all interactions.

### Our Standards

- Use welcoming and inclusive language
- Be respectful of differing viewpoints and experiences
- Gracefully accept constructive criticism
- Focus on what is best for the community
- Show empathy towards other community members

## Getting Started

### Prerequisites

Before contributing, ensure you have:

- Python 3.9+ installed
- Docker and Docker Compose
- Git configured with your name and email
- A GitHub account
- Basic understanding of REST APIs and database design

### First-Time Contributors

1. **Read the Documentation**: Start with the [README.md](README.md) and [Architecture Decision Record](docs/ADR.md)
2. **Set up Development Environment**: Follow the [Development Setup](#development-setup) guide
3. **Find an Issue**: Look for issues labeled `good-first-issue` or `help-wanted`
4. **Join the Discussion**: Comment on the issue you'd like to work on

## Development Setup

### 1. Fork and Clone

```bash
# Fork the repository on GitHub, then clone your fork
git clone https://github.com/YOUR_USERNAME/scoutconnect.git
cd scoutconnect

# Add upstream remote
git remote add upstream https://github.com/ORIGINAL_OWNER/scoutconnect.git
```

### 2. Environment Setup

```bash
# Copy environment template
cp .env.example .env

# Edit .env with your local settings
# Key variables:
# - DATABASE_URL
# - SECRET_KEY
# - DEBUG=True
```

### 3. Docker Development Environment

```bash
# Build and start development environment
docker-compose up --build

# Run in background
docker-compose up -d

# View logs
docker-compose logs -f web
```

### 4. Database Setup

```bash
# Run migrations
docker-compose exec web python manage.py migrate

# Create superuser (if using Django)
docker-compose exec web python manage.py createsuperuser

# Load sample data
docker-compose exec web python manage.py loaddata fixtures/sample_data.json
```

### 5. Verify Setup

```bash
# Run tests
docker-compose exec web python -m pytest

# Access the application
# API: http://localhost:8000
# Docs: http://localhost:8000/docs (FastAPI) or /admin (Django)
# Database: http://localhost:5050 (pgAdmin)
```

## Project Structure

```
scoutconnect/
├── app/                    # Main application code
│   ├── api/               # API endpoints
│   │   ├── v1/           # API version 1
│   │   │   ├── auth/     # Authentication endpoints
│   │   │   ├── players/  # Player management
│   │   │   ├── evaluations/ # Performance evaluations
│   │   │   └── sports/   # Sport configurations
│   ├── core/             # Core business logic
│   │   ├── models/       # Database models
│   │   ├── services/     # Business services
│   │   ├── scoring/      # Scoring algorithms
│   │   └── utils/        # Utility functions
│   ├── db/               # Database configuration
│   └── tests/            # Test files
├── docs/                 # Documentation
├── fixtures/             # Sample data
├── requirements/         # Python dependencies
├── docker-compose.yml    # Development environment
├── Dockerfile           # Container configuration
└── README.md            # Project overview
```

## Contributing Process

### 1. Choose Your Contribution

**Types of Contributions Welcome:**
- Bug fixes
- Feature implementations
- Documentation improvements
- Test coverage improvements
- Performance optimizations
- Code refactoring
- UI/UX improvements

### 2. Create a Branch

```bash
# Sync with upstream
git fetch upstream
git checkout main
git merge upstream/main

# Create feature branch
git checkout -b feature/your-feature-name
# or
git checkout -b bugfix/issue-number-description
```

### 3. Make Your Changes

- Write clean, maintainable code
- Follow coding standards
- Add appropriate tests
- Update documentation
- Commit frequently with clear messages

### 4. Test Your Changes

```bash
# Run full test suite
docker-compose exec web python -m pytest

# Run with coverage
docker-compose exec web python -m pytest --cov=app --cov-report=html

# Run linting
docker-compose exec web flake8 app/
docker-compose exec web black --check app/

# Run type checking (if using mypy)
docker-compose exec web mypy app/
```

## Coding Standards

### Python Style Guide

We follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) with some modifications:

```python
# Use Black for formatting
black app/

# Line length: 88 characters (Black default)
# Use double quotes for strings
# Use type hints for function signatures

def create_player_evaluation(
    player_id: int,
    evaluator_id: int,
    scores: Dict[str, float],
    notes: Optional[str] = None
) -> PlayerEvaluation:
    """Create a new player evaluation.
    
    Args:
        player_id: ID of the player being evaluated
        evaluator_id: ID of the evaluator (coach/scout)
        scores: Dictionary of evaluation scores
        notes: Optional evaluation notes
        
    Returns:
        Created PlayerEvaluation instance
        
    Raises:
        ValidationError: If scores are invalid
    """
    pass
```

### Database Models

```python
# Use descriptive model names
class PlayerEvaluation(BaseModel):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    evaluator = models.ForeignKey(User, on_delete=models.CASCADE)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    
    # Use clear field names
    overall_score = models.DecimalField(max_digits=4, decimal_places=2)
    evaluation_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'player_evaluations'
        ordering = ['-evaluation_date']
```

### API Endpoints

```python
# Use consistent naming and structure
@router.post("/players/{player_id}/evaluations/")
async def create_player_evaluation(
    player_id: int,
    evaluation: PlayerEvaluationCreate,
    current_user: User = Depends(get_current_user)
) -> PlayerEvaluationResponse:
    """Create a new player evaluation."""
    pass

# Always include proper HTTP status codes
# Use Pydantic models for request/response validation
# Include comprehensive docstrings
```

### Error Handling

```python
# Use custom exceptions
class PlayerNotFoundError(Exception):
    """Raised when a player cannot be found."""
    pass

# Handle errors gracefully
try:
    player = get_player_by_id(player_id)
except PlayerNotFoundError:
    raise HTTPException(
        status_code=404,
        detail=f"Player with ID {player_id} not found"
    )
```

## Testing Guidelines

### Test Structure

```python
# tests/test_evaluations.py
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

class TestPlayerEvaluations:
    """Test player evaluation functionality."""
    
    def test_create_evaluation_success(self, auth_headers, sample_player):
        """Test successful evaluation creation."""
        evaluation_data = {
            "sport_id": 1,
            "scores": {"speed": 8.5, "agility": 7.0},
            "notes": "Strong performance in speed tests"
        }
        
        response = client.post(
            f"/api/v1/players/{sample_player.id}/evaluations/",
            json=evaluation_data,
            headers=auth_headers
        )
        
        assert response.status_code == 201
        assert response.json()["overall_score"] > 0
    
    def test_create_evaluation_invalid_player(self, auth_headers):
        """Test evaluation creation with invalid player ID."""
        response = client.post(
            "/api/v1/players/99999/evaluations/",
            json={"sport_id": 1, "scores": {"speed": 8.5}},
            headers=auth_headers
        )
        
        assert response.status_code == 404
```

### Test Coverage Requirements

- **Minimum Coverage**: 85%
- **Critical Paths**: 100% (authentication, scoring algorithms, data validation)
- **Test Types**: Unit tests, integration tests, API tests

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_evaluations.py

# Run with coverage
pytest --cov=app --cov-report=html

# Run only failed tests
pytest --lf

# Run tests matching pattern
pytest -k "test_create_evaluation"
```

## Documentation

### Code Documentation

- **Docstrings**: All functions, classes, and modules must have docstrings
- **Type Hints**: Use type hints for all function parameters and return values
- **Comments**: Explain complex logic, not obvious code

### API Documentation

- **OpenAPI/Swagger**: Automatically generated from code
- **Examples**: Include request/response examples
- **Error Codes**: Document all possible error responses

### Update Documentation When:

- Adding new API endpoints
- Changing existing functionality
- Adding new configuration options
- Modifying database schema
- Adding new dependencies

## Issue Guidelines

### Before Creating an Issue

1. **Search existing issues** to avoid duplicates
2. **Check the documentation** for answers
3. **Try the latest version** to see if the issue is already fixed

### Issue Templates

**Bug Report:**
```markdown
## Bug Description
Brief description of the bug

## Steps to Reproduce
1. Step 1
2. Step 2
3. Step 3

## Expected Behavior
What should happen

## Actual Behavior
What actually happens

## Environment
- OS: [e.g., Ubuntu 20.04]
- Python version: [e.g., 3.9.7]
- Docker version: [e.g., 20.10.8]

## Additional Context
Any other relevant information
```

**Feature Request:**
```markdown
## Feature Description
Clear description of the proposed feature

## Use Case
Why is this feature needed?

## Proposed Solution
How should this feature work?

## Alternatives Considered
Other ways to solve this problem

## Additional Context
Any other relevant information
```

### Issue Labels

- `bug` - Something isn't working
- `enhancement` - New feature or request
- `documentation` - Improvements or additions to documentation
- `good-first-issue` - Good for newcomers
- `help-wanted` - Extra attention is needed
- `priority-high` - High priority issue
- `priority-low` - Low priority issue

## Pull Request Process

### Before Submitting

- [ ] Tests pass locally
- [ ] Code follows style guidelines
- [ ] Documentation is updated
- [ ] Commit messages are clear
- [ ] Branch is up to date with main

### PR Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## How Has This Been Tested?
- [ ] Unit tests
- [ ] Integration tests
- [ ] Manual testing

## Checklist
- [ ] My code follows the style guidelines of this project
- [ ] I have performed a self-review of my own code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes

## Screenshots (if applicable)
Add screenshots to help explain your changes

## Additional Notes
Any additional information or context
```

### Review Process

1. **Automated Checks**: CI pipeline must pass
2. **Peer Review**: At least one approval from a maintainer
3. **Testing**: Reviewer will test the changes
4. **Documentation**: Ensure documentation is adequate
5. **Merge**: Maintainer will merge when ready

### After Your PR is Merged

- Delete your feature branch
- Sync your fork with upstream
- Thank the reviewers!

## Release Process

### Version Numbering

We use [Semantic Versioning](https://semver.org/):
- **MAJOR.MINOR.PATCH** (e.g., 1.2.3)
- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes (backward compatible)

### Release Schedule

- **Patch releases**: As needed for critical bugs
- **Minor releases**: Monthly or bi-monthly
- **Major releases**: When significant breaking changes are needed

## Getting Help

### Communication Channels

- **GitHub Issues**: Technical problems and feature requests
- **Discussions**: General questions and ideas
- **Email**: [maintainer@scoutconnect.dev] for sensitive issues

### Resources

- [Project Documentation](docs/)
- [API Documentation](http://localhost:8000/docs)
- [Architecture Decision Record](docs/ADR.md)
- [Development Setup Guide](docs/development-setup.md)

## Recognition

Contributors will be recognized in:
- [CONTRIBUTORS.md](CONTRIBUTORS.md) file
- Release notes for significant contributions
- Annual contributor highlights

## License

By contributing to ScoutConnect, you agree that your contributions will be licensed under the same license as the project.

---

**Thank you for contributing to ScoutConnect!** 🎉

Your contributions help make talent discovery more accessible and effective for coaches and scouts worldwide.