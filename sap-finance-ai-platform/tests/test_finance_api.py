from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_create_finance_analysis() -> None:
    response = client.post(
        "/api/v1/finance/analyses",
        json={
            "company_code": "US01",
            "document_number": "TEST-INV-1001",
            "fiscal_year": 2026,
            "transaction_type": "vendor_invoice",
            "amount": 12500.75,
            "currency": "USD",
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["company_code"] == "US01"
    assert data["document_number"] == "TEST-INV-1001"
    assert data["amount"] == "12500.75"
    assert data["risk_level"] == "medium"
    assert data["status"] == "completed"


def test_list_finance_analyses() -> None:
    response = client.get("/api/v1/finance/analyses")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_finance_analysis_not_found() -> None:
    response = client.get("/api/v1/finance/analyses/999999")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Finance analysis not found",
    }