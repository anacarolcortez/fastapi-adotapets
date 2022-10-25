from fastapi.testclient import TestClient
import pytest
from test.utils.usuario_body import (
    create_user_admin, 
    create_invalid_user_deactivated,
    create_invalid_user_email, 
    create_valid_user
)
from src.server.database import get_collection
from src.routes import usuario

users_collection = get_collection("usuarios")

PREFIXO_URL = usuario.router.prefix


@pytest.fixture
def drop_user_table() -> bool:
    users_collection.delete_many({})
    return True

@pytest.fixture
def create_user(client: TestClient) -> bool:
    body = create_valid_user()
    response = client.post(PREFIXO_URL + "/", json=body)
    assert response.status_code == 201
    return response.json()


def test_should_create_user_for_adopter_with_correct_payload(client: TestClient, drop_user_table, create_user) -> None:
    assert drop_user_table == True
    body = create_valid_user()
    assert create_user["email"] == body["email"]

    
def test_should_not_create_duplicated_user_email(client: TestClient, drop_user_table, create_user) -> None:
    assert drop_user_table == True
    body = create_valid_user()
    assert create_user["email"] == body["email"]
    response = client.post(PREFIXO_URL + "/", json=body)
    data = response.json()
    assert response.status_code == 400
    assert data["detail"] == "Usuário já estava cadastrado no sistema"


def test_should_create_user_as_admin(client: TestClient, drop_user_table) -> None:
    assert drop_user_table == True
    body = create_user_admin()
    response = client.post(PREFIXO_URL + "/", json=body)
    data = response.json()
    assert response.status_code == 201
    assert data["admin"] == True
    

def test_should_not_create_user_deactivated(client: TestClient, drop_user_table) -> None:
    assert drop_user_table == True
    body = create_invalid_user_deactivated()
    response = client.post(PREFIXO_URL + "/", json=body)
    data = response.json()
    assert response.status_code == 201 #creates as active
    assert data["ativo"] == True
    

def test_should_not_create_user_invalid_email(client: TestClient, drop_user_table) -> None:
    assert drop_user_table == True
    body = create_invalid_user_email()
    response = client.post(PREFIXO_URL + "/", json=body)
    assert response.status_code == 422 
