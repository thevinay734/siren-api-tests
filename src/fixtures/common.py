import pytest
from src.core.api_client import APIClient


@pytest.fixture(scope="session")
def api_client():
    return APIClient()


@pytest.fixture(scope="session")
def device_headers():
    return {
        "deviceType": "web",
        "deviceToken": "web-cli",
        "language": "en",
        "timezone": "Asia/Kolkata",
        "deviceIp": "127.0.0.1",
    }

