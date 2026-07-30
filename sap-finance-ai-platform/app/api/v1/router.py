from fastapi import APIRouter

from app.api.routes.finance import router as finance_router
from app.api.routes.health import router as health_router

api_router = APIRouter()

api_router.include_router(health_router)
api_router.include_router(finance_router)

## code app\api\v1\router.py                                                     
