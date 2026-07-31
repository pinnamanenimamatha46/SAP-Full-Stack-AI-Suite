from decimal import Decimal

from app.ai.risk_engine import calculate_risk


def test_high_value_transaction_is_high_risk() -> None:
    result = calculate_risk(
        amount=Decimal("150000.00"),
        transaction_type="international_transfer",
        company_code="US01",
        currency="USD",
    )

    assert result.risk_score >= 70
    assert result.risk_level == "high"
    assert result.fraud_probability >= 0.70
    assert result.recommended_actions


def test_standard_invoice_is_low_risk() -> None:
    result = calculate_risk(
        amount=Decimal("2500.00"),
        transaction_type="vendor_invoice",
        company_code="US01",
        currency="USD",
    )

    assert result.risk_level == "low"
    assert result.risk_score < 40
