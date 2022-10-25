from fastapi.testclient import TestClient
import pytest
from src.security.basic_oauth import validate_admin
from fastapi.security import HTTPBasicCredentials
from main import app


def override_validate_admin(credentials: HTTPBasicCredentials):
    return True


app.dependency_overrides[validate_admin] = override_validate_admin


@pytest.fixture(scope="function")
def client():
    with TestClient(app) as c:
        yield c