from fastapi.testclient import TestClient
from src.security.basic_oauth import validate_admin

import pytest
from main import app



@pytest.fixture(scope="function")
def client():
    app.dependency_overrides[validate_admin] = True
    with TestClient(app) as c:
        yield c
        
        
"""
Idealmente, seria possível passar o banco de dados como dependência em cada rota e 
sobrescrever essa dependência nas configurações do teste, passando um banco de dados 
de teste.
Neste projeto, porém, aponto para um banco de dados diferente do banco de produção,
na variável de ambiente.
"""