import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from src.config import config

DEFAULT_TIMEOUT = 10


class TimeoutSession(requests.Session):
    def __init__(self, timeout: int):
        super().__init__()
        self._timeout = timeout

    def request(self, *args, **kwargs):
        if "timeout" not in kwargs:
            kwargs["timeout"] = self._timeout
        return super().request(*args, **kwargs)


class APIClient:
    def __init__(self, base_url=config.BASE_URL):
        self.base_url = base_url.rstrip("/")
        self.session = TimeoutSession(DEFAULT_TIMEOUT)
        self.session.headers.update(config.HEADERS)

        retry = Retry(
            total=3,
            backoff_factor=0.5,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["HEAD", "GET", "OPTIONS", "POST", "PUT", "PATCH", "DELETE"],
        )
        adapter = HTTPAdapter(max_retries=retry)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)

    def _url(self, endpoint: str) -> str:
        return f"{self.base_url}/{endpoint.lstrip('/')}"

    def get(self, endpoint, headers=None):
        return self.session.get(self._url(endpoint), headers=headers)

    def post(self, endpoint, data=None, headers=None):
        return self.session.post(self._url(endpoint), json=data, headers=headers)

    def patch(self, endpoint, data=None, headers=None):
        return self.session.patch(self._url(endpoint), json=data, headers=headers)

    def delete(self, endpoint, headers=None):
        return self.session.delete(self._url(endpoint), headers=headers)
