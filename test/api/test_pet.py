from fastapi.testclient import TestClient
import pytest
from test.utils.pet_body import create_invalid_adopted_pet, create_invalid_pet_size, create_invalid_pet_type, create_valid_pet, update_pet_data
from src.server.database import get_collection
from src.routes import pet

pets_collection = get_collection("pets")


PREFIXO_URL = pet.router.prefix


@pytest.fixture
def get_fake_admin() -> dict:
    return "teste@teste.com", "123senh@"
    #validação é ignorada com override de dependência


@pytest.fixture
def drop_pets_table() -> bool:
    pets_collection.delete_many({})
    return True


@pytest.fixture
def create_pet(client: TestClient, get_fake_admin) -> dict:
    body = create_valid_pet()
    body["username"], body["password"] = get_fake_admin
    response = client.post(PREFIXO_URL + "/cadastro", json=body)
    assert response.status_code == 201
    return response.json()


def test_should_create_pet_with_correct_payload(client: TestClient, drop_pets_table, create_pet) -> None:
    assert drop_pets_table == True
    body = create_valid_pet()
    pet = create_pet
    assert pet["nome"] == body["nome"]


def test_should_not_create_duplicated_pet_name(client: TestClient, drop_pets_table, create_pet, get_fake_admin) -> None:
    assert drop_pets_table == True
    body =  create_valid_pet()
    body["username"], body["password"] = get_fake_admin
    pet = create_pet
    assert pet["nome"] == body["nome"]
    response = client.post(PREFIXO_URL + "/cadastro", json=body)
    data = response.json()
    assert response.status_code == 400
    assert data["detail"] == "Pet já estava cadastrado no sistema"


def test_should_not_create_adopted_pet(client: TestClient, drop_pets_table, get_fake_admin) -> None:
    assert drop_pets_table == True
    body =  create_invalid_adopted_pet()
    body["username"], body["password"] = get_fake_admin
    response = client.post(PREFIXO_URL + "/cadastro", json=body)
    data = response.json()
    assert response.status_code == 201 #forces 'adotado = False'
    assert data["nome"] == body["nome"]
    assert data["adotado"] == False


def test_should_return_error_when_pet_type_is_wrong(client: TestClient, drop_pets_table, get_fake_admin):
    assert drop_pets_table == True
    body =  create_invalid_pet_type()
    body["username"], body["password"] = get_fake_admin
    response = client.post(PREFIXO_URL + "/cadastro", json=body)
    data = response.text
    assert response.status_code == 422 
    assert "value is not a valid enumeration member; permitted: 'cachorro', 'gato'" in data


def test_should_return_error_when_pet_size_is_wrong(client: TestClient, drop_pets_table, get_fake_admin):
    assert drop_pets_table == True
    body =  create_invalid_pet_size()
    body["username"], body["password"] = get_fake_admin
    response = client.post(PREFIXO_URL + "/cadastro", json=body)
    data = response.text
    assert response.status_code == 422 
    assert "value is not a valid enumeration member; permitted: 'pequeno', 'medio', 'grande'" in data


def test_should_return_pet_info_by_pet_name(client: TestClient, drop_pets_table, create_pet):
    assert drop_pets_table == True
    pet = create_pet
    response = client.get(PREFIXO_URL + f"/cadastro/{pet['nome']}")
    assert response.status_code == 200
    data = response.json()
    assert data["nome"] == pet["nome"]


def test_should_return_pets_list(client: TestClient, drop_pets_table, create_pet):
    assert drop_pets_table == True
    pet = create_pet
    response = client.get(PREFIXO_URL + "/lista")
    assert response.status_code == 200
    data = response.text
    assert pet["nome"] in data


def test_should_update_pet_info(client: TestClient, drop_pets_table, create_pet, get_fake_admin):
    assert drop_pets_table == True
    pet = create_pet
    body =  update_pet_data()
    body["username"], body["password"] = get_fake_admin
    response = client.patch(PREFIXO_URL + f"/cadastro/{pet['nome']}", json=body)
    assert response.status_code == 200
    data = response.json()
    assert data["pcd"] == body["pcd"]
    assert data["foto"] == body["foto"]
    assert data["obs"] == body["obs"]


# def test_should_delete_pet(client: TestClient, drop_pets_table, create_pet, get_fake_admin):
#     assert drop_pets_table == True
#     pet = create_pet
#     username, password = get_fake_admin
#     response = client.delete(PREFIXO_URL + f"/cadastro/{pet['nome']}", auth=(username, password))
#     assert response.status_code == 200
#     data = response.text
#     assert "Pet removido do sistema" in data