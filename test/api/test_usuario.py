from fastapi.testclient import TestClient

from test.utils.user_body import create_valid_user
from src.routes import usuario

PREFIXO_URL = usuario.router.prefix

def test_create_user(client: TestClient) -> None:
    body = create_valid_user()
    response = client.post(PREFIXO_URL + "/", json=body)
    data = response.json()
    assert body["email"] == data["email"]
