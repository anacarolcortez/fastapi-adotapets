from fastapi.testclient import TestClient
import pytest
from test.utils.pet_body import create_valid_pet
from test.utils.usuario_body import create_user_admin
from src.routes import pet, usuario


PREFIXO_URL_PET = pet.router.prefix
PREFIXO_URL_USUARIO = usuario.router.prefix


@pytest.fixture
def create_admin_user(client: TestClient) -> int:
    body = create_user_admin()
    response = client.post(PREFIXO_URL_USUARIO + "/", json=body)
    return response.status_code


# def test_should_create_pet_with_correct_payload(client: TestClient, create_admin_user) -> None:
#     assert create_admin_user == 201
#     body = create_valid_pet()
#     response = client.post(PREFIXO_URL_PET + "/", json=body)
#     # override dependência e passar usuário?
#     data = response.json()
#     assert response.status_code == 201
#     assert body["nome"] == data["nome"]
