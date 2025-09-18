import uuid
from src.core.api_client import APIClient
from src.config import config

client = APIClient()


# ✅ Positive: User SignUp
def test_user_signup_positive(device_headers):
    unique = uuid.uuid4().hex[:8]
    payload = {
        "name": f"Rajesh-{unique}",
        "email": f"rajesh_{unique}@yopmail.com",
        "countryCode": "91",
        "phoneNumber": f"98{unique}",
        "dob": "2001-01-15",
        "password1": "Password@123",
        "password2": "Password@123",
    }

    response = client.post("/user/auth/signUp", data=payload, headers=device_headers)
    assert response.status_code in [200, 201], response.text
    body = response.json()
    assert "data" in body


# ❌ Negative: SignUp with same number
def test_user_signup_duplicate():
    payload = {
        "countryCode": config.USER_COUNTRY_CODE,
        "phoneNumber": config.USER_MOBILE,  # already registered
        "password": "Password@123",
        "name": "Duplicate User",
    }
    response = client.post("/user/auth/signUp", data=payload)
    assert response.status_code in [400, 409]
