from fastapi.testclient import TestClient
import pytest
from test.utils.pet_body import create_valid_pet
from test.utils.usuario_body import create_user_admin
from src.routes import pet, usuario


PREFIXO_URL_PET = pet.router.prefix
PREFIXO_URL_USUARIO = usuario.router.prefix


@pytest.fixture
def get_fake_admin() -> dict:
    return "teste@teste.com", "123senh@"
    #validação é ignorada com override de dependência


def test_should_create_pet_with_correct_payload(client: TestClient, get_fake_admin) -> None:
    body = create_valid_pet()
    body["username"], body["password"] = get_fake_admin
    response = client.post(PREFIXO_URL_PET + "/cadastro", json=body)
    data = response.json()
    print(data)
    assert response.status_code == 201
    assert body["nome"] == data["nome"]
