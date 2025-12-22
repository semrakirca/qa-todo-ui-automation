import pytest

pytestmark = pytest.mark.skip(reason="Reqres is protected by Cloudflare (403 challenge). Not stable for CI.")

import requests
BASE_URL = "https://reqres.in"


def test_list_users_returns_200_and_has_data():
    url = f"{BASE_URL}/api/users?page=2"

    response = requests.get(url, timeout=10)

    assert response.status_code == 200

    body = response.json()
    assert "data" in body
    assert isinstance(body["data"], list)
    assert len(body["data"]) > 0


def test_get_single_user_returns_expected_fields():
    user_id = 2
    url = f"{BASE_URL}/api/users/{user_id}"

    response = requests.get(url, timeout=10)

    assert response.status_code == 200

    body = response.json()
    assert "data" in body

    user = body["data"]
    assert user["id"] == user_id
    assert "email" in user
    assert "first_name" in user
    assert "last_name" in user
    assert user["email"].endswith("@reqres.in")


def test_get_non_existing_user_returns_404():
    # Negative test (çok sorulur)
    url = f"{BASE_URL}/api/users/23"

    response = requests.get(url, timeout=10)

    assert response.status_code == 404
