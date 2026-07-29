from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field


class FinanceAnalysisCreate(BaseModel):
    company_code: str = Field(min_length=1, max_length=20)
    document_number: str = Field(min_length=1, max_length=50)
    fiscal_year: int = Field(ge=2000, le=2100)
    transaction_type: str = Field(min_length=1, max_length=50)
    amount: Decimal = Field(gt=0, decimal_places=2)
    currency: str = Field(min_length=3, max_length=3)
    risk_level: str = Field(min_length=1, max_length=20)
    status: str = Field(min_length=1, max_length=30)
    findings: str | None = None


class FinanceAnalysisResponse(FinanceAnalysisCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime