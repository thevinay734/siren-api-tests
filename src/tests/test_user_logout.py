from src.core.api_client import APIClient


client = APIClient()


def test_user_logout(auth_headers, device_headers):
    headers = {**auth_headers, **device_headers}
    response = client.get("/user/auth/logout", headers=headers)
    assert response.status_code in [200, 401], response.text
