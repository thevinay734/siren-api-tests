from src.core.api_client import APIClient

client = APIClient()


def test_user_orders_list(auth_headers):
    response = client.get("/user/orders/list?page=1&perPage=5", headers=auth_headers)
    assert response.status_code == 200


def test_place_order(auth_headers):
    payload = {
        "productId": "12345",
        "quantity": 2,
        "paymentMethod": "COD",
    }
    response = client.post("/user/orders/create", data=payload, headers=auth_headers)
    assert response.status_code in [200, 201]
