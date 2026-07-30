from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.finance_analysis import FinanceAnalysis
from app.schemas.finance_analysis import FinanceAnalysisCreate


def create_finance_analysis(
    db: Session,
    payload: FinanceAnalysisCreate,
) -> FinanceAnalysis:
    record = FinanceAnalysis(**payload.model_dump())

    db.add(record)
    db.commit()
    db.refresh(record)

    return record


def list_finance_analyses(
    db: Session,
    skip: int = 0,
    limit: int = 100,
) -> list[FinanceAnalysis]:
    statement = (
        select(FinanceAnalysis)
        .order_by(FinanceAnalysis.id.desc())
        .offset(skip)
        .limit(limit)
    )

    return list(db.scalars(statement).all())


def get_finance_analysis(
    db: Session,
    analysis_id: int,
) -> FinanceAnalysis | None:
    return db.get(FinanceAnalysis, analysis_id)


def delete_finance_analysis(
    db: Session,
    analysis_id: int,
) -> bool:
    record = db.get(FinanceAnalysis, analysis_id)

    if record is None:
        return False

    db.delete(record)
    db.commit()

    return True