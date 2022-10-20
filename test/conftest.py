from email.generator import Generator
from fastapi.testclient import TestClient
import pytest
from main import app



@pytest.fixture(scope="function")
def client() -> Generator:
    with TestClient(app) as c:
        yield c
        
        
"""
Para não poluir o banco em produção, será preciso passar as coleções
como dependência em cada rota. Sobrescrever as dependências no teste,
passando um banco de dados de teste.
Atualmente, altera-se o nome do bd no arquivo server/database,
mas não é o ideal.
Corrigir
"""