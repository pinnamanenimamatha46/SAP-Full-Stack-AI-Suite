from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.ai.risk_engine import calculate_risk
from app.models.finance_analysis import FinanceAnalysis
from app.schemas.finance_analysis import (
    FinanceAnalysisCreate,
    FinanceAnalysisUpdate,
)


def create_finance_analysis(
    db: Session,
    payload: FinanceAnalysisCreate,
) -> FinanceAnalysis:
    risk_assessment = calculate_risk(
        amount=payload.amount,
        transaction_type=payload.transaction_type,
        company_code=payload.company_code,
        currency=payload.currency,
    )

    analysis = FinanceAnalysis(
        company_code=payload.company_code,
        document_number=payload.document_number,
        fiscal_year=payload.fiscal_year,
        transaction_type=payload.transaction_type,
        amount=payload.amount,
        currency=payload.currency,
        risk_level=risk_assessment.risk_level,
        status="completed",
        findings=risk_assessment.explanation,
    )

    db.add(analysis)
    db.commit()
    db.refresh(analysis)

    return analysis


def list_finance_analyses(
    db: Session,
    skip: int = 0,
    limit: int = 100,
) -> list[FinanceAnalysis]:
    return db.query(FinanceAnalysis).offset(skip).limit(limit).all()


def get_finance_analysis(
    db: Session,
    analysis_id: int,
) -> FinanceAnalysis | None:
    return db.get(FinanceAnalysis, analysis_id)


def update_finance_analysis(
    db: Session,
    analysis_id: int,
    payload: FinanceAnalysisUpdate,
) -> FinanceAnalysis:
    analysis = db.get(FinanceAnalysis, analysis_id)

    if analysis is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Finance analysis not found.",
        )

    risk_assessment = calculate_risk(
        amount=payload.amount,
        transaction_type=payload.transaction_type,
        company_code=payload.company_code,
        currency=payload.currency,
    )

    analysis.company_code = payload.company_code
    analysis.document_number = payload.document_number
    analysis.fiscal_year = payload.fiscal_year
    analysis.transaction_type = payload.transaction_type
    analysis.amount = payload.amount
    analysis.currency = payload.currency
    analysis.risk_level = risk_assessment.risk_level
    analysis.status = "completed"
    analysis.findings = risk_assessment.explanation

    db.commit()
    db.refresh(analysis)

    return analysis


def delete_finance_analysis(
    db: Session,
    analysis_id: int,
) -> bool:
    analysis = db.get(FinanceAnalysis, analysis_id)

    if analysis is None:
        return False

    db.delete(analysis)
    db.commit()

    return True
