from src.controllers.enderecos import (
    create_address,
    find_address,
    update_address,
    delete_address
)

from fastapi import APIRouter, Depends
from src.schemas.endereco import EnderecoSchema
from src.security.basic_oauth import validate_adopter


router = APIRouter(prefix="/adotantes/endereco")


@router.post("/{email}", tags=["adotantes"])
async def register_client_address(address: EnderecoSchema, email:str=Depends(validate_adopter)):
    try:
        return await create_address(
            address,
            email
        )
    except Exception as e:
        return e


@router.get("/{email}", tags=["adotantes"])
async def get_client_address(email:str=Depends(validate_adopter)):
    try:
        return await find_address(
            email
        )
    except Exception as e:
        return e
   
    
@router.put("/{email}", tags=["adotantes"])
async def update_client_address(address: EnderecoSchema, email:str=Depends(validate_adopter)):
    try:
        return await update_address(
            address,
            email
        )
    except Exception as e:
        return e
    
    
@router.delete("/{email}", tags=["adotantes"])
async def delete_client_address(email:str=Depends(validate_adopter)):
    try:
        return await delete_address(
            email
        )
    except Exception as e:
        return e