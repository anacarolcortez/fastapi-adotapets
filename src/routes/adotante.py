from src.controllers.adotantes import (
    create_adopter,
    delete_adopter_info,
    find_adopter,
    get_all_adopters,
    update_adopter_info, 
)

from fastapi import APIRouter, Depends

from src.security.basic_oauth import validate_admin, validate_adopter
from src.schemas.adotante import AdotanteUsuarioSchema, AdotanteUpdateSchema

router = APIRouter(prefix="/adotantes")


@router.post("/", tags=["adotantes"])
async def register_adopter(adopter: AdotanteUsuarioSchema):
    try:
        return await create_adopter(
            adopter
        )
    except Exception as e:
        return e


@router.get("/{email}", tags=["adotantes"])
async def get_adopter(email:str=Depends(validate_adopter)):
    try:
        return await find_adopter(
            email
        )
    except Exception as e:
        return e
    
    
@router.get("/", tags=["adotantes"])
async def list_adopters(user=Depends(validate_admin)):
    try:
        if user:
            return await get_all_adopters(
                skip = 0,
                limit = 10
            )
    except Exception as e:
        return e
    
@router.patch("/{email}", tags=["adotantes"])
async def update_adopter_data(data: AdotanteUpdateSchema, email:str=Depends(validate_adopter)):
    try:
        return await update_adopter_info(
            email,
            data
        )
    except Exception as e:
        return e            


@router.delete("/{email}", tags=["adotantes"])
async def delete_adopter(email:str=Depends(validate_adopter)):
    try:
        return await delete_adopter_info(
            email
        )
    except Exception as e:
        return e