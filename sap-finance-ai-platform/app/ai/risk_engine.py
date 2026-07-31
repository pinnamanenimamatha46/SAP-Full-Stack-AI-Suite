from decimal import Decimal

from app.schemas.risk import RiskAssessment


def calculate_risk(
    *,
    amount: Decimal,
    transaction_type: str,
    company_code: str,
    currency: str,
) -> RiskAssessment:
    score = 10
    reasons: list[str] = []
    actions: list[str] = []

    if amount >= Decimal("100000"):
        score += 45
        reasons.append("Transaction amount exceeds 100,000.")
    elif amount >= Decimal("50000"):
        score += 30
        reasons.append("Transaction amount exceeds 50,000.")
    elif amount >= Decimal("10000"):
        score += 15
        reasons.append("Transaction amount exceeds 10,000.")

    high_risk_types = {
        "manual_journal_entry",
        "cash_payment",
        "vendor_refund",
        "international_transfer",
    }

    if transaction_type.lower() in high_risk_types:
        score += 25
        reasons.append(
            f"Transaction type '{transaction_type}' requires additional review."
        )

    if currency.upper() not in {"USD", "EUR", "GBP", "INR"}:
        score += 10
        reasons.append("The transaction uses a less commonly monitored currency.")

    if not company_code.strip():
        score += 20
        reasons.append("Company code is missing.")

    score = min(score, 100)
    fraud_probability = round(score / 100, 2)

    if score >= 70:
        risk_level = "high"
        actions.extend(
            [
                "Place the transaction on hold.",
                "Require manual finance approval.",
                "Validate vendor and payment details.",
            ]
        )
    elif score >= 40:
        risk_level = "medium"
        actions.extend(
            [
                "Route the transaction for secondary review.",
                "Verify supporting SAP documents.",
            ]
        )
    else:
        risk_level = "low"
        actions.append("Continue standard processing.")

    explanation = (
        " ".join(reasons)
        if reasons
        else "No significant risk indicators were detected."
    )

    return RiskAssessment(
        risk_score=score,
        risk_level=risk_level,
        fraud_probability=fraud_probability,
        explanation=explanation,
        recommended_actions=actions,
    )
