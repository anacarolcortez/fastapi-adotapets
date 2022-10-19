from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder

from src.services.endereco import (
    create_client_address, delete_address_by_email, 
    get_address_by_adopter_email, update_address_by_email
)


async def create_address(address, email):
    address_exists = await get_address_by_adopter_email(email)
    if address_exists:
        raise HTTPException(status_code=400, detail="Adotante já possui endereço cadastrado. Edite o atual.")
    address_data = jsonable_encoder(address)
    address = await create_client_address(address_data, email)
    if address is not None:
        return address    
    raise HTTPException(status_code=400, detail="Erro na criação do endereço do adotante")


async def find_address(email):
    address = await get_address_by_adopter_email(email)
    if address:
        return address
    raise HTTPException(status_code=404, detail="Não há endereço cadastrado para o adotante")


async def update_address(address, email):
    address_data = jsonable_encoder(address)
    updated_address = await update_address_by_email(address_data, email)
    if updated_address:
        return await get_address_by_adopter_email(email)
    raise HTTPException(status_code=400, detail="Erro ao atualizar endereço")
    

async def delete_address(email):
    deleted_address = await delete_address_by_email(email)
    if deleted_address:
        return {
            "status_code": 200,
            "detail": "Endereço removido do sistema",
            "headers": None
        }
    raise HTTPException(status_code=400, detail="Erro ao excluir endereço: não encontrado no sistema")
