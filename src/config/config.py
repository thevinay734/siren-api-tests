import os

# Base configuration loaded from environment variables to avoid committing secrets
BASE_URL = os.getenv("BASE_URL", "http://13.204.67.134:3001/api/v1")

# User credentials (mobile login) loaded from env; defaults are empty to force explicit configuration
USER_COUNTRY_CODE = os.getenv("USER_COUNTRY_CODE", "+91")
USER_MOBILE = os.getenv("USER_MOBILE", "")
USER_PASSWORD = os.getenv("USER_PASSWORD", "")

# Default headers for JSON APIs
HEADERS = {
    "Content-Type": "application/json"
}

# Do not store mutable runtime state here; tests should pass tokens via fixtures

