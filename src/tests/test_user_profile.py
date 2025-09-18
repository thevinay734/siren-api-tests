from src.core.api_client import APIClient

client = APIClient()


# ✅ Positive: Fetch profile
def test_user_profile(auth_headers, user_login):
    response = client.get(f"/user/details/{user_login['user_id']}", headers=auth_headers)
    assert response.status_code == 200


# ❌ Negative: Fetch profile without token
def test_user_profile_without_token(user_login):
    response = client.get(f"/user/details/{user_login['user_id']}")
    assert response.status_code == 401
