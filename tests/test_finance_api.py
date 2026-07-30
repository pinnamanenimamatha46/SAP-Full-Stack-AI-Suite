def test_update_finance_analysis() -> None:
    create_response = client.post(
        "/api/v1/finance/analyses",
        json={
            "company_code": "US01",
            "document_number": "TEST-UPDATE-1001",
            "fiscal_year": 2026,
            "transaction_type": "vendor_invoice",
            "amount": 10000.00,
            "currency": "USD",
        },
    )

    assert create_response.status_code == 201

    analysis_id = create_response.json()["id"]

    update_response = client.put(
        f"/api/v1/finance/analyses/{analysis_id}",
        json={
            "company_code": "US01",
            "document_number": "TEST-UPDATE-1001-UPDATED",
            "fiscal_year": 2026,
            "transaction_type": "vendor_invoice",
            "amount": 15000.00,
            "currency": "USD",
        },
    )

    assert update_response.status_code == 200

    data = update_response.json()

    assert data["id"] == analysis_id
    assert data["document_number"] == "TEST-UPDATE-1001-UPDATED"
    assert data["amount"] == "15000.00"


def test_update_finance_analysis_not_found() -> None:
    response = client.put(
        "/api/v1/finance/analyses/999999",
        json={
            "company_code": "US01",
            "document_number": "NOT-FOUND",
            "fiscal_year": 2026,
            "transaction_type": "vendor_invoice",
            "amount": 1000.00,
            "currency": "USD",
        },
    )

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Finance analysis not found.",
    }


def test_delete_finance_analysis() -> None:
    create_response = client.post(
        "/api/v1/finance/analyses",
        json={
            "company_code": "US01",
            "document_number": "TEST-DELETE-1001",
            "fiscal_year": 2026,
            "transaction_type": "vendor_invoice",
            "amount": 5000.00,
            "currency": "USD",
        },
    )

    assert create_response.status_code == 201

    analysis_id = create_response.json()["id"]

    delete_response = client.delete(
        f"/api/v1/finance/analyses/{analysis_id}",
    )

    assert delete_response.status_code == 204
    assert delete_response.content == b""

    get_response = client.get(
        f"/api/v1/finance/analyses/{analysis_id}",
    )

    assert get_response.status_code == 404


def test_delete_finance_analysis_not_found() -> None:
    response = client.delete(
        "/api/v1/finance/analyses/999999",
    )

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Finance analysis not found",
    }