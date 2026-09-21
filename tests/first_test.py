from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Welcome To my payment Website!"
    }


def test_deposit():
    response = client.post(
        "/payments/deposite/Fathy",
        json={
            "payment_type": "paypal",
            "amount": 100
        }
    )

    assert response.status_code == 200
    assert response.json() == "This paid 100.0 using Paypal"


def test_withdraw():
    response = client.post(
        "/payments/withdraw/Fathy",
        json={
            "payment_type": "paypal",
            "amount": 50
        }
    )

    assert response.status_code == 200
    assert response.json() == "This paid 50.0 using Paypal"