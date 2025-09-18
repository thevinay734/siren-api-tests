import pytest
from src.config import config


@pytest.fixture(scope="session")
def user_login(api_client, device_headers):
    payload = {
        "countryCode": config.USER_COUNTRY_CODE.lstrip("+"),
        "phoneNumber": config.USER_MOBILE,
        "password": config.USER_PASSWORD,
    }
    resp = api_client.post("/user/auth/signIn", data=payload, headers=device_headers)
    assert resp.status_code == 200, resp.text
    data = resp.json()["data"]
    return {"token": data["accessToken"], "user_id": data["_id"]}


@pytest.fixture()
def auth_headers(user_login):
    return {"Authorization": f"Bearer {user_login['token']}"}

