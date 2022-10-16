from fastapi import APIRouter, Depends
from src.controllers.adocoes import (
    create_adoption_request,
    get_all_adoptions_by_email,
    get_all_adoptions_by_pet
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
    
    
@router.get("/{email}", tags=["adocoes"])
async def list_adoptions_by_email(email:str=Depends(validate_adopter)):
    try:
        return await get_all_adoptions_by_email(
            adoptions_collection,
            email,
            skip = 0,
            limit = 10
        )
    except Exception as e:
        return e
    

@router.get("/adotantes/{email}", tags=["adocoes"])
async def admin_list_adoptions_by_email(email: str, admin:str=Depends(validate_admin)):
    try:
        if admin:
            return await get_all_adoptions_by_email(
                adoptions_collection,
                email,
                skip = 0,
                limit = 10
            )
    except Exception as e:
        return e
    

@router.get("/pets/{nome_pet}", tags=["adocoes"])
async def admin_list_adoptions_by_pet(nome_pet: str, admin:str=Depends(validate_admin)):
    try:
        if admin:
            return await get_all_adoptions_by_pet(
                adoptions_collection,
                nome_pet,
                skip = 0,
                limit = 10
            )
    except Exception as e:
        return e