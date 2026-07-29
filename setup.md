##*********************************************************************************
                            # SAP-Full-Stack-AI-Suite
##*********************************************************************************

##  1)  Create a project:
        ## mkdir SAP-Full-Stack-AI-Suite

##  1a) cd into the created project
        ## cd SAP-Full-Stack-AI-Suite

##  1b) from cmd go into the vscode
        ## code .

##  1c) Verify location:
        ## Get-Location

##  2)  Initialize the parent project:
        ## git init
        ## git branch -M main

##  2a) Verify:
        ## pwd
        ## git status

        ## repository root : git rev-parse --show-toplevel

##  2b) Create the main folders:

        ##  mkdir docs
        ##  mkdir architecture
        ##  mkdir shared-infrastructure
        ## mkdir .github
        ##  mkdir scripts
        ##  mkdir deployments
        ##  mkdir monitoring
        ##  mkdir templates

##  2c) Create placeholder files:

        ##  New-Item docs\.gitkeep -ItemType File
        ##  New-Item architecture\.gitkeep -ItemType File
        ##  New-Item shared-infrastructure\.gitkeep -ItemType File
        ##  New-Item .\architecture\.gitkeep -ItemType File -Force
        ##  New-Item .\deployments\.gitkeep -ItemType File -Force
        ##  New-Item .\docs\.gitkeep -ItemType File -Force
        ##  New-Item .\monitoring\.gitkeep -ItemType File -Force
        ##  New-Item .\scripts\.gitkeep -ItemType File -Force
        ##  New-Item .\shared-infrastructure\.gitkeep -ItemType File -Force
        ##  New-Item .\templates\.gitkeep -ItemType File -Force
        ##  New-Item .\.github\.gitkeep -ItemType File -Force

##  2d) check git status
        ## git status

##  2e) README.md:

# SAP Full Stack AI Suite

Enterprise-grade Full Stack AI platforms built for SAP business processes using modern AI, Generative AI, Agentic AI, and cloud-native technologies.

---

## Overview

SAP Full Stack AI Suite is a collection of enterprise AI applications that demonstrate how Artificial Intelligence can be integrated with SAP business processes across multiple industries.

The suite is designed as a single parent Git repository where every SAP AI platform is maintained as a folder inside the main project.

This repository serves as an enterprise portfolio for Full Stack AI Engineering using modern software architecture and best development practices.

---

# Repository Structure

```text
SAP-Full-Stack-AI-Suite/
│
├── .github/
├── architecture/
├── deployments/
├── docs/
├── monitoring/
├── scripts/
├── shared-infrastructure/
├── templates/
│
├── sap-finance-ai-platform/
├── sap-human-capital-ai-platform/
├── sap-procurement-ai-platform/
├── sap-sales-ai-platform/
├── sap-supply-chain-ai-platform/
├── sap-manufacturing-ai-platform/
├── sap-healthcare-ai-platform/
├── sap-banking-ai-platform/
├── sap-retail-ai-platform/
├── sap-telecom-ai-platform/
│
├── README.md
└── setup.md
```

---

# SAP AI Platforms

| Platform | Domain |
|----------|--------|
| SAP Finance AI Platform | Financial Analytics, Invoice Processing, Risk Analysis |
| SAP Human Capital AI Platform | HR Analytics, Recruiting, Workforce Intelligence |
| SAP Procurement AI Platform | Vendor Intelligence, Purchase Optimization |
| SAP Sales AI Platform | Forecasting, Opportunity Scoring |
| SAP Supply Chain AI Platform | Inventory Prediction, Logistics Optimization |
| SAP Manufacturing AI Platform | Predictive Maintenance, Production Analytics |
| SAP Healthcare AI Platform | Clinical Intelligence, Patient Analytics |
| SAP Banking AI Platform | Fraud Detection, Credit Risk, Compliance |
| SAP Retail AI Platform | Demand Forecasting, Customer Insights |
| SAP Telecom AI Platform | Network Analytics, Customer Support |

---

# Technology Stack

## Backend

- Python
- FastAPI
- SQLAlchemy
- Pydantic
- Alembic

## Frontend

- Streamlit
- React
- HTML
- CSS
- JavaScript

## Databases

- PostgreSQL
- MongoDB
- Redis

## AI & Machine Learning

- OpenAI
- LangChain
- LangGraph
- CrewAI
- AutoGen
- MCP
- Agentic AI

## DevOps

- Docker
- Docker Compose
- Kubernetes
- GitHub Actions
- Nginx

## Monitoring

- Prometheus
- Grafana

---

# Common Project Structure

Each SAP AI platform follows a consistent architecture.

```text
platform-name/
│
├── app/
├── api/
├── services/
├── models/
├── schemas/
├── repositories/
├── ai/
├── tests/
├── docker/
├── docs/
├── requirements/
└── README.md
```

---

# Features

- Enterprise AI APIs
- REST API Architecture
- SAP Business Workflows
- AI Agents
- Retrieval-Augmented Generation (RAG)
- Prompt Engineering
- Document Intelligence
- Predictive Analytics
- Authentication
- Audit Logging
- Monitoring Dashboard
- Docker Deployment
- Kubernetes Ready

---

# Development Workflow

1. Clone repository

```bash
git clone <repository-url>
```

2. Enter project

```bash
cd SAP-Full-Stack-AI-Suite
```

3. Create virtual environment

```bash
uv venv
```

4. Activate environment

Windows

```powershell
.venv\Scripts\activate
```

5. Install dependencies

```bash
uv sync
```

6. Run FastAPI

```bash
uv run uvicorn app.main:app --reload
```

---

# Documentation

- Architecture
- API Documentation
- Deployment Guide
- Monitoring Guide
- Development Standards

Documentation is available in the **docs/** folder.

---

# Future Roadmap

- SAP AI Copilot
- Multi-Agent SAP Automation
- SAP Workflow Intelligence
- SAP Document Processing
- SAP Knowledge Graph
- SAP Analytics Dashboard
- AI Chat Assistant
- SAP Integration Services
- CI/CD Pipelines
- Enterprise Monitoring

---

# License

This project is intended for portfolio, and enterprise demonstration purposes.

# Author

**Mamatha Pinnamaneni**

Full Stack AI Developer

Enterprise AI | SAP AI | Generative AI | Agentic AI | FastAPI | Python | Docker | Kubernetes

##  2f) .gitignore:

# ==========================================================
# SAP Full Stack AI Suite
# Parent Repository .gitignore
# ==========================================================

# ----------------------------------------------------------
# Python
# ----------------------------------------------------------
__pycache__/
*.py[cod]
*$py.class

# ----------------------------------------------------------
# Virtual Environments
# ----------------------------------------------------------
.venv/
venv/
env/
ENV/

# ----------------------------------------------------------
# Environment Variables
# ----------------------------------------------------------
.env
.env.*
!.env.example

# ----------------------------------------------------------
# Python Build
# ----------------------------------------------------------
build/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# ----------------------------------------------------------
# uv
# ----------------------------------------------------------
.python-version

# Keep lock file if desired
# uv.lock

# ----------------------------------------------------------
# IDE
# ----------------------------------------------------------
.vscode/
.idea/

# ----------------------------------------------------------
# Jupyter
# ----------------------------------------------------------
.ipynb_checkpoints/

# ----------------------------------------------------------
# Testing
# ----------------------------------------------------------
.pytest_cache/
.coverage
coverage.xml
htmlcov/
.tox/
.nox/
.mypy_cache/
.ruff_cache/

# ----------------------------------------------------------
# Logs
# ----------------------------------------------------------
logs/
*.log

# ----------------------------------------------------------
# Database
# ----------------------------------------------------------
*.sqlite
*.sqlite3

# ----------------------------------------------------------
# Docker
# ----------------------------------------------------------
docker-compose.override.yml

# ----------------------------------------------------------
# Kubernetes
# ----------------------------------------------------------
*.kubeconfig

# ----------------------------------------------------------
# Secrets
# ----------------------------------------------------------
*.pem
*.key
*.crt
*.p12

# ----------------------------------------------------------
# macOS
# ----------------------------------------------------------
.DS_Store

# ----------------------------------------------------------
# Windows
# ----------------------------------------------------------
Thumbs.db
Desktop.ini

# ----------------------------------------------------------
# Temporary Files
# ----------------------------------------------------------
*.tmp
*.temp
*.swp
*.swo
*~

# ----------------------------------------------------------
# Node
# ----------------------------------------------------------
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# ----------------------------------------------------------
# Streamlit
# ----------------------------------------------------------
.streamlit/secrets.toml

# ----------------------------------------------------------
# Alembic
# ----------------------------------------------------------
alembic/versions/__pycache__/

# ----------------------------------------------------------
# PyCharm
# ----------------------------------------------------------
.idea/

# ----------------------------------------------------------
# VS Code Workspace
# ----------------------------------------------------------
*.code-workspace

# ----------------------------------------------------------
# Local Configuration
# ----------------------------------------------------------
local_settings.py

# ----------------------------------------------------------
# Cache
# ----------------------------------------------------------
.cache/

# ----------------------------------------------------------
# Terraform
# ----------------------------------------------------------
.terraform/
*.tfstate
*.tfstate.*

# ----------------------------------------------------------
# Miscellaneous
# ----------------------------------------------------------
*.bak
*.orig
*.rej

# ----------------------------------------------------------
# Git
# ----------------------------------------------------------
.gitmodules

##  2g) First Commit
        ## git add .
        ##  git commit -m "Initial SAP Full Stack AI Suite repository structure"
        ##  git remote add origin https://github.com/pinnamanenimamatha46/SAP-Full-Stack-AI-Suite.git
        ##  git pudh main origin

##  3) create and cd first child Project: sap-finance-ai-platform

        ##  mkdir sap-finance-ai-platform
        ##  cd sap-finance-ai-platform

##  3a)  Initialize the child project with uv
        uv init --app --python 3.11 --vcs none

        ## uv sync

##  3b) Create & activateenv
        ## uv venv .venv --python 3.11

        ## Activate .venv: .venv\Scripts\activate

##  2c) Add FastAPI dependencies:
        ## uv add fastapi uvicorn pydantic-settings sqlalchemy psycopg alembic

##  2d) Add development dependencies:
        ## uv add --dev pytest pytest-asyncio httpx ruff

##  2e) Remove the default main.py
        ## Remove-Item main.py

## 2f)  Create the application folders:

$folders = @(
    "app",
    "app\api",
    "app\api\v1",
    "app\api\routes",
    "app\ai",
    "app\core",
    "app\db",
    "app\models",
    "app\repositories",
    "app\schemas",
    "app\services",
    "tests",
    "docs",
    "docker",
    "k8s",
    "scripts"
)

$folders | ForEach-Object {
    New-Item -ItemType Directory -Path $_ -Force
}

##  2g) Create Python package files:

$files = @(
    "app\__init__.py",
    "app\api\__init__.py",
    "app\api\v1\__init__.py",
    "app\api\v1\router.py",
    "app\api\routes\__init__.py",
    "app\api\routes\health.py",
    "app\ai\__init__.py",
    "app\core\__init__.py",
    "app\db\__init__.py",
    "app\models\__init__.py",
    "app\repositories\__init__.py",
    "app\schemas\__init__.py",
    "app\services\__init__.py",
    "app\main.py",
    "tests\__init__.py",
    "tests\test_health.py",
    ".env.example"
)

$files | ForEach-Object {
    New-Item -ItemType File -Path $_ -Force
}

##  2h)  Add the health endpoint:
         ## code app\api\routes\health.py

from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def health_check() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "sap-finance-ai-platform",
    }

##  2i) Add the API router:
        code app\api\v1\router.py

from fastapi import APIRouter

from app.api.routes.health import router as health_router

api_router = APIRouter()

api_router.include_router(
    health_router,
    tags=["Health"],
)

##  2j) Create the FastAPI application
        ## code app\main.py
from fastapi import FastAPI

from app.api.v1.router import api_router

app = FastAPI(
    title="SAP Finance AI Platform",
    description="Enterprise SAP Finance AI APIs",
    version="0.1.0",
)

app.include_router(api_router, prefix="/api/v1")


@app.get("/")
async def root() -> dict[str, str]:
    return {
        "message": "SAP Finance AI Platform API",
        "status": "running",
        "docs": "/docs",
    }

##  2k) health route: code app\api\routes\health.py

from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def health_check() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "sap-finance-ai-platform",
    }

##  2l) Confirm package files exist
        ## Get-ChildItem app -Recurse

##  2m) test the import from the current child-project folder:
        ##  uv run python -c "from app.main import app; print(app.title)"
        ## SAP Finance AI Platform

##  2n) Start the fast API:
        uv run uvicorn app.main:app --reload
        http://127.0.0.1:8000
        http://127.0.0.1:8000/docs
        http://127.0.0.1:8000/api/v1/health

##  2o)`test the full application import:
        ## OpenAPI schema to list the actual endpoints:
        ## uv run python -c "from app.main import app; print(list(app.openapi()['paths'].keys()))"
        
        #   ['/api/v1/health', '/']

## ## start application
        uv run uvicorn app.main:app --reload

##  2p) Test the root endpoint:
        ## Invoke-RestMethod http://127.0.0.1:8000/

        ## Test the health endpoint: 
        Invoke-RestMethod http://127.0.0.1:8000/api/v1/health

        ## Open Swagger: http://127.0.0.1:8000/docs

## 2A)  Add PostgreSQL:
        ## Install dependencies:
            ##  uv add sqlalchemy psycopg alembic
        
        ## use OpenAPI to inspect registered endpoints:
            uv run python -c "from app.main import app; print(list(app.openapi()['paths'].keys()))"
        
        ## start the server: uv run uvicorn app.main:app --reload

        ## Test:
            ## Invoke-RestMethod http://127.0.0.1:8000/
            ## Invoke-RestMethod http://127.0.0.1:8000/api/v1/health
        ##  Start:
            Start-Process http://127.0.0.1:8000/docs
        
##  2B) create the first automated health test.
        ## code tests\test_health.py

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "running"


def test_health() -> None:
    response = client.get("/api/v1/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": "sap-finance-ai-platform",
    }

##  2C) Run Tests:
        ## uv run pytest -v
        ## 2 passed 1 warning in 0.92s

##  2D) create the database configuration:

        ## code .env
            APP_NAME=SAP Finance AI Platform
            APP_VERSION=0.1.0
            DATABASE_URL=postgresql+psycopg://sap_finance:sap_finance_password@localhost:5435/sap_finance_ai
        
        ## Settings file: code app\core\config.py

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "SAP Finance AI Platform"
    app_version: str = "0.1.0"
    database_url: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()

        ## Verify .env loads correctly:
        
            ## uv run python -c "from app.core.config import settings; print(settings.app_name); print(settings.database_url)"

            ## SAP Finance AI Platformpostgresql+psycopg://sap_finance:sap_finance_password@localhost:5435/sap_finance_ai

##  2E) Create the SQLAlchemy base
        ## code app\db\base.py
        
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass
        
        ##  database session: code app\db\session.py

from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.core.config import settings

engine = create_engine(
    settings.database_url,
    pool_pre_ping=True,
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

        ## test - database modules:

##  2f) install the binary Psycopg driver: uv add "psycopg[binary]"

##  Verify Psycopg: uv run python -c "import psycopg; print('Psycopg version:', psycopg.__version__); print('Implementation:', psycopg.pq.__impl__)"

Psycopg version: 3.3.4
Implementation: binary

##  Retry your original command
    uv run python -c "from app.db.session import engine, SessionLocal; print(engine.url); print(SessionLocal)"

    ##  postgresql+psycopg://sap_finance:***@localhost:5435/sap_finance_ai
        sessionmaker(class_='Session', autocommit=False, bind=Engine(postgresql+psycopg://sap_finance:***@localhost:5435/sap_finance_ai), autoflush=False, expire_on_commit=True)

## Test an actual database connection
    uv run python -c "from sqlalchemy import text; from app.db.session import engine; conn = engine.connect(); print(conn.execute(text('SELECT 1')).scalar()); conn.close()"

## Display the database host and port
uv run python -c "from app.db.session import engine; print(engine.url.render_as_string(hide_password=True))"

## compose.yml

services:
  postgres:
    image: postgres:17-alpine
    container_name: sap-finance-postgres
    restart: unless-stopped

    environment:
      POSTGRES_USER: sap_finance
      POSTGRES_PASSWORD: sap_finance_password
      POSTGRES_DB: sap_finance_ai

    ports:
      - "5435:5432"

    volumes:
      - sap_finance_postgres_data:/var/lib/postgresql/data

    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U sap_finance -d sap_finance_ai"]
      interval: 5s
      timeout: 5s
      retries: 10

volumes:
  sap_finance_postgres_data:

## Get-Content .env
APP_NAME=SAP Finance AI Platform
APP_VERSION=0.1.0
DATABASE_URL=postgresql+psycopg://sap_finance:sap_finance_password@localhost:5435/sap_finance_ai

##  
