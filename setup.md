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
        ## uv init --app --python 3.11
        ## git init
        ## git branch -M main

##  2a) Verify:
        ## pwd
        ## uv --version:    0.11.18
        ## git status

        ## repository root : git rev-parse --show-toplevel

##  2b) Create the main folders:

        ##  mkdir docs
        ##  mkdir architecture
        ##  mkdir shared-infrastructure

##  2c) Create placeholder files:

        ##  New-Item docs\.gitkeep -ItemType File
        ##  New-Item architecture\.gitkeep -ItemType File
        ##  New-Item shared-infrastructure\.gitkeep -ItemType File

##  3) create and cd first child Project: sap-finance-ai-platform

        ##  mkdir sap-finance-ai-platform
        ##  cd sap-finance-ai-platform

##  4)  Initialize the child project with uv
        uv init --app --python 3.11 --vcs none

        ## uv sync

##  5)  Test the starter application:
        ## uv run python main.py
        ##  Hello from sap-finance-ai-platform!

##  6)  Add 
        ##  the initial backend dependencies:
            ##  uv add fastapi "uvicorn[standard]" pydantic pydantic-settings sqlalchemy psycopg[binary] alembic

        ## development dependencies:
        ##  uv add --dev pytest pytest-asyncio httpx ruff

        ##  uv sync










Commit the initial project:

        ## git status
        ## git add .
        ## git commit -m "Initialize SAP Finance AI Platform"
        
##        ##
        ##