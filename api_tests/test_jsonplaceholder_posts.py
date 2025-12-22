
def test_list_posts_returns_200_and_list(api, base_url):
    url = f"{base_url}/posts"
    r = api.get(url, timeout=10)

    assert r.status_code == 200

    body = r.json()
    assert isinstance(body, list)
    assert len(body) > 0
    assert {"userId", "id", "title", "body"}.issubset(body[0].keys())


def test_get_single_post_returns_expected_id(api, base_url):
    post_id = 1
    url = f"{base_url}/posts/{post_id}"
    r = api.get(url, timeout=10)

    assert r.status_code == 200, f"Expected 200 but got {r.status_code}. Body: {r.text[:200]}"

    body = r.json()
    assert body["id"] == post_id
    assert isinstance(body["title"], str)
    assert isinstance(body["body"], str)



def test_create_post_returns_201_and_echoes_payload(api, base_url):
    url = f"{base_url}/posts"
    payload = {
        "title": "Semra QA API test",
        "body": "This is a test post body",
        "userId": 1,
    }

    r = api.post(url, json=payload, timeout=10)

    assert r.status_code == 201

    body = r.json()
    assert body["title"] == payload["title"]
    assert body["body"] == payload["body"]
    assert body["userId"] == payload["userId"]
    assert "id" in body


def test_get_non_existing_post_returns_empty_object_or_404(api, base_url):
    url = f"{base_url}/posts/9999"
    r = api.get(url, timeout=10)

    assert r.status_code in (200, 404)

    if r.status_code == 200:
        assert r.json() == {}





# import requests

# BASE_URL = "https://jsonplaceholder.typicode.com"


# def test_list_posts_returns_200_and_list():
#     url = f"{BASE_URL}/posts"
#     r = requests.get(url, timeout=10)

#     assert r.status_code == 200

#     body = r.json()
#     assert isinstance(body, list)
#     assert len(body) > 0
#     # schema sniff
#     assert "userId" in body[0]
#     assert "id" in body[0]
#     assert "title" in body[0]
#     assert "body" in body[0]


# def test_get_single_post_returns_expected_id():
#     post_id = 1
#     url = f"{BASE_URL}/posts/{post_id}"
#     r = requests.get(url, timeout=10)

#     assert r.status_code == 200

#     body = r.json()
#     assert body["id"] == post_id
#     assert isinstance(body["title"], str)
#     assert isinstance(body["body"], str)


# def test_create_post_returns_201_and_echoes_payload():
#     url = f"{BASE_URL}/posts"
#     payload = {
#         "title": "Semra QA API test",
#         "body": "This is a test post body",
#         "userId": 1,
#     }

#     r = requests.post(url, json=payload, timeout=10)

#     assert r.status_code == 201

#     body = r.json()
#     # JSONPlaceholder create simülasyonu: payload'ı geri döner + id verir
#     assert body["title"] == payload["title"]
#     assert body["body"] == payload["body"]
#     assert body["userId"] == payload["userId"]
#     assert "id" in body


# def test_get_non_existing_post_returns_empty_object_or_404():
#     """
#     Negative test:
#     JSONPlaceholder genelde 404 yerine {} döndürebiliyor.
#     Bu yüzden "davranışa dayalı" assertion yazıyoruz.
#     """
#     url = f"{BASE_URL}/posts/9999"
#     r = requests.get(url, timeout=10)

#     assert r.status_code in (200, 404)

#     if r.status_code == 200:
#         body = r.json()
#         assert body == {}  # boş obje dönmesi beklenen davranış
