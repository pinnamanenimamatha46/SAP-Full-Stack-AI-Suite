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
