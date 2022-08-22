from fastapi.testclient import TestClient

from app.config import settings


def test_read_now(
    client: TestClient
) -> None:
    response = client.get(
        f"{settings.API_V1_STR}/weather/now",
        headers={'Accept': 'application/json'},
        params={'public_ip': '85.53.20.2'}
    )
    assert response.status_code == 200
    content = response.json()
    assert content


def test_read_now_bad(
    client: TestClient
) -> None:
    response = client.get(
        f"{settings.API_V1_STR}/weather/now",
        headers={'Accept': 'application/json'},
        params={'public_ip': 'BAD IP'}
    )
    assert response.status_code == 422


def test_read_now_bad_2(
    client: TestClient
) -> None:
    response = client.get(
        f"{settings.API_V1_STR}/weather/now",
        headers={'Accept': 'application/json'}
    )
    assert response.status_code == 422
