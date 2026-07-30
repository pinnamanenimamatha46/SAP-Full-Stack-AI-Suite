from fastapi import APIRouter, Depends, HTTPException, Query, Response, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.finance_analysis import (
    FinanceAnalysisCreate,
    FinanceAnalysisResponse,
)
from app.services.finance_service import (
    create_finance_analysis,
    delete_finance_analysis,
    get_finance_analysis,
    list_finance_analyses,
)

router = APIRouter(
    prefix="/finance",
    tags=["Finance"],
)


@router.post(
    "/analyses",
    response_model=FinanceAnalysisResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_analysis(
    payload: FinanceAnalysisCreate,
    db: Session = Depends(get_db),
) -> FinanceAnalysisResponse:
    return create_finance_analysis(
        db=db,
        payload=payload,
    )


@router.get(
    "/analyses",
    response_model=list[FinanceAnalysisResponse],
)
def get_analyses(
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=100, ge=1, le=500),
    db: Session = Depends(get_db),
) -> list[FinanceAnalysisResponse]:
    return list_finance_analyses(
        db=db,
        skip=skip,
        limit=limit,
    )


@router.get(
    "/analyses/{analysis_id}",
    response_model=FinanceAnalysisResponse,
)
def get_analysis(
    analysis_id: int,
    db: Session = Depends(get_db),
) -> FinanceAnalysisResponse:
    record = get_finance_analysis(
        db=db,
        analysis_id=analysis_id,
    )

    if record is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Finance analysis not found",
        )

    return record


@router.delete(
    "/analyses/{analysis_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_analysis(
    analysis_id: int,
    db: Session = Depends(get_db),
) -> Response:
    deleted = delete_finance_analysis(
        db=db,
        analysis_id=analysis_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Finance analysis not found",
        )

    return Response(status_code=status.HTTP_204_NO_CONTENT)

