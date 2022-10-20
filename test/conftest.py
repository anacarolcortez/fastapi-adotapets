from email.generator import Generator
from fastapi.testclient import TestClient
import pytest
from main import app



@pytest.fixture(scope="function")
def client() -> Generator:
    with TestClient(app) as c:
        yield c
        
        
"""
Na "vida real", o deploy em produção aponta para um banco diferente do banco de
desenvolvimento e de teste.
Idealmente, seria possível passar o banco de dados como dependência em cada rota e 
sobrescrever essa dependência nas configurações do teste, passando um banco de dados 
de teste, independente dos demais.
Neste projeto, utilizo um banco de dados diferente do que foi colocado em produção,
informando uma chave distinta.
"""