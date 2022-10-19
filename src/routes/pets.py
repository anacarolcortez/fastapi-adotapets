from src.controllers.pets import (
    create_pet,
    find_pet,
    get_all_pets,
    update_pet_info,
    delete_pet_info
)

from fastapi import APIRouter, Depends
from src.security.basic_oauth import validate_admin
from src.server.database import db

from src.schemas.pet import PetSchema, PetUpdateSchema


router = APIRouter(prefix="/pets")


@router.post("/", tags=["pets"])
async def register_pet(pet: PetSchema, user=Depends(validate_admin)):
    try:
        if user:
            return await create_pet(
                pet
            )
    except Exception as e:
        return e


@router.get("/{name}", tags=["pets"])
async def get_pet(name: str):
    try:
        return await find_pet(
            name
        )
    except Exception as e:
        return e
    
    
@router.get("/", tags=["pets"])
async def list_pets():
    try:
        return await get_all_pets(
            skip = 0,
            limit = 10
        )
    except Exception as e:
        return e
    
    
@router.patch("/{name}", tags=["pets"])
async def update_pet_data(name: str, data: PetUpdateSchema, user=Depends(validate_admin)):
    try:
        if user:
            return await update_pet_info(
                name,
                data
            )
    except Exception as e:
        return e
                

@router.delete("/{name}", tags=["pets"])
async def delete_pet(name: str, user=Depends(validate_admin)):
    try:
        if user:
            return await delete_pet_info(
                name
            )
    except Exception as e:
        return e