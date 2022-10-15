from src.controllers.adotantes import (
    create_adopter,
    delete_adopter_info,
    find_adopter,
    get_all_adopters,
    update_adopter_info, 
)

from fastapi import APIRouter, Depends, HTTPException
from src.server.database import db

from src.security.basic_oauth import validate_admin, validate_adopter
from src.schemas.adotante import AdotanteUsuarioSchema, AdotanteUpdateSchema

router = APIRouter(prefix="/adotantes")
adopters_collection = db.adopters_collection
users_collection = db.users_collection


@router.post("/", tags=["adotantes"])
async def register_adopter(adopter: AdotanteUsuarioSchema):
    try:
        return await create_adopter(
            adopters_collection,
            users_collection,
            adopter
        )
    except Exception as e:
        return e


@router.get("/{email}", tags=["adotantes"])
async def get_adopter(email:str=Depends(validate_adopter)):
    try:
        return await find_adopter(
            adopters_collection,
            email
        )
    except Exception as e:
        return e
    
    
@router.get("/", tags=["adotantes"])
async def list_adopters(user=Depends(validate_admin)):
    try:
        if user:
            return await get_all_adopters(
                adopters_collection,
                skip = 0,
                limit = 10
            )
    except Exception as e:
        return e
    
@router.patch("/{email}", tags=["adotantes"])
async def update_adopter_data(data: AdotanteUpdateSchema, email:str=Depends(validate_adopter)):
    try:
        return await update_adopter_info(
            adopters_collection,
            email,
            data
        )
    except Exception as e:
        return e            


@router.delete("/{email}", tags=["adotantes"])
async def delete_adopter(email:str=Depends(validate_adopter)):
    try:
        return await delete_adopter_info(
            adopters_collection,
            users_collection,
            email
        )
    except Exception as e:
        return e