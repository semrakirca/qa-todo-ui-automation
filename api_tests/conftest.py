import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

@pytest.fixture(scope="session")
def api():
    s = requests.Session()
    s.headers.update({
        "Accept": "application/json",
        "User-Agent": "qa-automation-tests/1.0",
    })
    return s
