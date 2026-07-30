from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class FinanceAnalysisCreate(BaseModel):
    company_code: str
    document_number: str
    fiscal_year: int
    transaction_type: str
    amount: Decimal
    currency: str


class FinanceAnalysisUpdate(BaseModel):
    company_code: str
    document_number: str
    fiscal_year: int
    transaction_type: str
    amount: Decimal
    currency: str


class FinanceAnalysisResponse(BaseModel):
    id: int
    company_code: str
    document_number: str
    fiscal_year: int
    transaction_type: str
    amount: Decimal
    currency: str
    risk_level: str
    status: str
    findings: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
