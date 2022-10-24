from fastapi import APIRouter, Depends, HTTPException, status
from src.controllers.pet import (
    create_pet,
    find_pet,
    get_all_pets,
    update_pet_info,
    delete_pet_info
)
from src.security.basic_oauth import validate_admin
from src.schemas.pet import PetSchema, PetUpdateSchema
from src.utils.custom_exceptions import NotDeletedException, NotFoundException, NotInsertedException, NotUpdatedException


router = APIRouter(prefix="/pets")


@router.post("/cadastro", status_code=status.HTTP_201_CREATED, tags=["pets"])
async def admin_register_pet(pet: PetSchema, user=Depends(validate_admin)):
    try:
        if user:
            return await create_pet(
                pet
            )
    except NotInsertedException as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=e.msg)


@router.get("/cadastro/{name}", tags=["pets"])
async def get_pet(name: str):
    try:
        return await find_pet(
            name
        )
    except NotFoundException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=e.msg)


@router.get("/lista", tags=["pets"])
async def list_pets_to_adoption():
    try:
        return await get_all_pets(
            skip=0,
            limit=10
        )
    except NotFoundException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=e.msg)


@router.patch("/cadastro/{name}", tags=["pets"])
async def admin_update_pet_data(name: str, data: PetUpdateSchema, user=Depends(validate_admin)):
    try:
        if user:
            return await update_pet_info(
                name,
                data
            )
    except NotUpdatedException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=e.msg)


@router.delete("/cadastro/{name}", tags=["pets"])
async def admin_delete_pet(name: str, user=Depends(validate_admin)):
    try:
        if user:
            return await delete_pet_info(
                name
            )
    except NotDeletedException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=e.msg)
