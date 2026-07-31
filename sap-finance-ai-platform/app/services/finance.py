from sqlalchemy.orm import Session

from app.ai.risk_engine import calculate_risk
from app.models.finance import FinanceAnalysis
from app.schemas.finance import FinanceAnalysisCreate


def create_finance_analysis(
    db: Session,
    analysis_data: FinanceAnalysisCreate,
) -> FinanceAnalysis:
    risk_assessment = calculate_risk(
        amount=analysis_data.amount,
        transaction_type=analysis_data.transaction_type,
        company_code=analysis_data.company_code,
        currency=analysis_data.currency,
    )

    db_analysis = FinanceAnalysis(
        company_code=analysis_data.company_code,
        document_number=analysis_data.document_number,
        fiscal_year=analysis_data.fiscal_year,
        transaction_type=analysis_data.transaction_type,
        amount=analysis_data.amount,
        currency=analysis_data.currency,
        risk_level=risk_assessment.risk_level,
        status="completed",
        findings=risk_assessment.explanation,
    )

    db.add(db_analysis)
    db.commit()
    db.refresh(db_analysis)

    return db_analysis
