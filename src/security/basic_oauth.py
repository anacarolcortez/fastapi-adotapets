import secrets
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials


from src.server.database import get_collection
users_collection = get_collection("usuarios")


security = HTTPBasic()


async def validate_adopter(credentials: HTTPBasicCredentials = Depends(security)):
    adopter = await validate_credentials(credentials)
    return adopter["email"]


async def validate_admin(credentials: HTTPBasicCredentials = Depends(security)):
    user = await validate_credentials(credentials)
    is_admin = user["admin"]
    if is_admin:
        return True
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Apenas administradores podem acessar esses dados",
        headers={"WWW-Authenticate": "Basic"},
    )


async def validate_credentials(credentials):
    current_username = credentials.username.encode("utf8")
    current_password = credentials.password.encode("utf8")
    
    user = await get_user_credentials(current_username)

    is_correct_username = secrets.compare_digest(
        current_username, user["email"].encode("utf8")
    )

    is_correct_password = secrets.compare_digest(
        current_password, user["senha"].encode("utf8")
    )
    
    if not (is_correct_username and is_correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="E-mail ou senha incorretos",
            headers={"WWW-Authenticate": "Basic"},
        )
        
    return user


async def get_user_credentials(current_username):
    current_username = current_username.decode("utf8")
    response = await users_collection.find_one({'email': current_username})
    if response is not None:
        is_active = response["ativo"]
        if is_active:
            return response
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Usuário inativo",
            headers={"WWW-Authenticate": "Basic"},
        )
    raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Usuário não cadastrado no sistema",
            headers={"WWW-Authenticate": "Basic"},
        )