from datetime import datetime
from decimal import Decimal

from sqlalchemy import DateTime, Integer, Numeric, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class FinanceAnalysis(Base):
    __tablename__ = "finance_analyses"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    company_code: Mapped[str] = mapped_column(
        String(10),
        nullable=False,
        index=True,
    )

    document_number: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        index=True,
    )

    fiscal_year: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    transaction_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    amount: Mapped[Decimal] = mapped_column(
        Numeric(15, 2),
        nullable=False,
    )

    currency: Mapped[str] = mapped_column(
        String(3),
        nullable=False,
    )

    risk_level: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        default="low",
    )

    status: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        default="pending",
    )

    findings: Mapped[str] = mapped_column(
        Text,
        nullable=False,
        default="No findings available.",
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )