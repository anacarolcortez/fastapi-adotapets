from src.controllers.enderecos import (
    create_address,
    #find_address,
)

from fastapi import APIRouter, Depends
from src.schemas.endereco import EnderecoSchema
from src.server.database import db
from src.security.basic_oauth import validate_adopter


router = APIRouter(prefix="/enderecos")
address_collection = db.address_collection


@router.post("/{email}", tags=["enderecos"])
async def register_client_address(address: EnderecoSchema, email:str=Depends(validate_adopter)):
    try:
        return await create_address(
            address_collection,
            address,
            email
        )
    except Exception as e:
        return e

