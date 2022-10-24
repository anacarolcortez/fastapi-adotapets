from fastapi import APIRouter, Depends, HTTPException, status
from src.controllers.adotante import (
    create_adopter,
    delete_adopter_info,
    find_adopter,
    get_all_adopters,
    update_adopter_info,
)
from src.security.basic_oauth import validate_admin, validate_adopter
from src.schemas.adotante import AdotanteSchema, AdotanteUpdateSchema
from src.utils.custom_exceptions import NotDeletedException, NotFoundException, NotInsertedException, NotUpdatedException


router = APIRouter(prefix="/adotantes")


@router.post("/cadastro/{email}", status_code=status.HTTP_201_CREATED, tags=["adotantes"])
async def register_adopter(adopter: AdotanteSchema, email: str = Depends(validate_adopter)):
    try:
        return await create_adopter(
            adopter,
            email
        )
    except NotInsertedException as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=e.msg)


@router.get("/cadastro/{email}", tags=["adotantes"])
async def get_adopter(email: str = Depends(validate_adopter)):
    try:
        return await find_adopter(
            email
        )
    except NotFoundException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=e.msg)


@router.get("/lista", tags=["adotantes"])
async def admin_list_adopters(user=Depends(validate_admin)):
    try:
        if user:
            return await get_all_adopters(
                skip=0,
                limit=10
            )
    except NotFoundException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=e.msg)


@router.patch("/cadastro/{email}", tags=["adotantes"])
async def update_adopter_data(data: AdotanteUpdateSchema, email: str = Depends(validate_adopter)):
    try:
        return await update_adopter_info(
            email,
            data
        )
    except NotUpdatedException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=e.msg)


@router.delete("/{email}", tags=["adotantes"])
async def delete_adopter(email: str = Depends(validate_adopter)):
    try:
        return await delete_adopter_info(
            email
        )
    except NotDeletedException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=e.msg)
