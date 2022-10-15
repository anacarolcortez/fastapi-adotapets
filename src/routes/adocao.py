from fastapi import APIRouter, Depends
from src.controllers.adocoes import (
    create_adoption_request
)
from src.schemas.adocao import PedidoAdocaoSchema
from src.server.database import db
from src.security.basic_oauth import validate_admin, validate_adopter


router = APIRouter(prefix="/adocoes")
adopters_collection = db.adopters_collection
pets_collection = db.pets_collection
address_collection = db.address_collection
adoptions_collection = db.adoptions_collection


@router.post("/{email}/{pet_name}", tags=["adocoes"])
async def register_adoption_request(pet_name: str, request: PedidoAdocaoSchema, email:str=Depends(validate_adopter)):
    try:
        return await create_adoption_request(
            adopters_collection,
            address_collection,
            pets_collection,
            adoptions_collection,
            request,
            email,
            pet_name
        )
    except Exception as e:
        return e