from src.core.api_client import APIClient
from src.config import config

client = APIClient()


# ✅ Positive: Login with mobile + password
def test_user_login_positive(user_login):
    assert user_login["token"]


# ❌ Negative: Wrong password
def test_user_login_wrong_password():
    payload = {
        "countryCode": config.USER_COUNTRY_CODE,
        "phoneNumber": config.USER_MOBILE,
        "password": "WrongPass@123",
    }
    response = client.post("/user/auth/signIn", data=payload)
    assert response.status_code in [400, 401, 403]
