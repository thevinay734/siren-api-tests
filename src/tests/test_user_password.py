from src.core.api_client import APIClient
from src.config import config

client = APIClient()


# ✅ Positive: Change password
def test_change_password(auth_headers):
    payload = {"oldPassword": config.USER_PASSWORD, "newPassword": "NewPass@123"}
    response = client.patch("/user/auth/change_password", data=payload, headers=auth_headers)
    assert response.status_code == 200


# ❌ Negative: Wrong old password
def test_change_password_wrong_old(auth_headers):
    payload = {"oldPassword": "WrongOld123", "newPassword": "AnotherPass@123"}
    response = client.patch("/user/auth/change_password", data=payload, headers=auth_headers)
    assert response.status_code in [400, 401]
