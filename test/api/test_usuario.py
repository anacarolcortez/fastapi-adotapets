from fastapi.testclient import TestClient
from test.utils.user_body import (
    create_invalid_admin, 
    create_invalid_user_deactivated, 
    create_valid_user
)
from src.routes import usuario


PREFIXO_URL = usuario.router.prefix


def test_should_create_user_for_adopter_with_correct_payload(client: TestClient) -> None:
    body = create_valid_user()
    response = client.post(PREFIXO_URL + "/", json=body)
    data = response.json()
    assert body["email"] == data["email"]
    
    
def test_should_not_create_duplicated_user_email(client: TestClient) -> None:
    body = create_valid_user()
    response = client.post(PREFIXO_URL + "/", json=body)
    data = response.json()
    assert response.status_code == 400
    assert data["detail"] == "Usuário já estava cadastrado no sistema"


def test_should_not_create_user_as_admin(client: TestClient) -> None:
    body = create_invalid_admin()
    response = client.post(PREFIXO_URL + "/", json=body)
    data = response.json()
    assert data["admin"] == False
    

def test_should_not_create_user_deactivated(client: TestClient) -> None:
    body = create_invalid_user_deactivated()
    response = client.post(PREFIXO_URL + "/", json=body)
    data = response.json()
    assert data["ativo"] == True
    
