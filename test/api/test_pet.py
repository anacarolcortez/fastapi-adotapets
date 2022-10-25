from fastapi.testclient import TestClient
from test.utils.pet_body import (
    create_valid_pet
)
from src.routes import pet


PREFIXO_URL = pet.router.prefix

#aqui precisa fazer override da autenticação
def test_should_create_pet_with_correct_payload(client: TestClient):
    body = create_valid_pet()
    response = client.post(PREFIXO_URL + "/", json=body)
    data = response.json()
    assert response.status_code == 201
    assert body["nome"] == data["nome"]