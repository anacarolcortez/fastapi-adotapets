from fastapi import HTTPException

from src.services.endereco import create_client_address, get_address_by_adopter_email


async def create_address(address_collection, address, email):
    address_exists = await get_address_by_adopter_email(address_collection, email)
    if address_exists:
        raise HTTPException(status_code=400, detail="Adotante já possui endereço cadastrado. Edite o atual.")
    address = await create_client_address(address_collection, address, email)
    if address is not None:
        return address    
    raise HTTPException(status_code=400, detail="Erro na criação do endereço do adotante")
