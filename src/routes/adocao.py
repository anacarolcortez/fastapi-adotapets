from fastapi import APIRouter, Depends, HTTPException, status
from src.controllers.adocao import (
    create_adoption_request,
    get_all_adoptions_by_email,
    get_all_adoptions_by_pet,
    update_request_status
)
from src.schemas.adocao import PedidoAdocaoSchema, StatusAdocaoSchema
from src.security.basic_oauth import validate_admin, validate_adopter
from src.utils.custom_exceptions import NotFoundException, NotUpdatedException, RulesException


router = APIRouter(prefix="/adocoes")


@router.post("/{email}/{nome_pet}", status_code=status.HTTP_201_CREATED, tags=["adocoes"])
async def register_adoption_request(nome_pet: str, request: PedidoAdocaoSchema, email: str = Depends(validate_adopter)):
    try:
        return await create_adoption_request(
            request,
            email,
            nome_pet
        )
    except NotFoundException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=e.msg)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=e.msg)


@router.get("/{email}", tags=["adocoes"])
async def list_adopter_requests(email: str = Depends(validate_adopter)):
    try:
        return await get_all_adoptions_by_email(
            email,
            skip=0,
            limit=10
        )
    except NotFoundException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=e.msg)


@router.get("/adotantes/{email}", tags=["adocoes"])
async def admin_list_adoptions_by_email(email: str, admin: str = Depends(validate_admin)):
    try:
        if admin:
            return await get_all_adoptions_by_email(
                email,
                skip=0,
                limit=10
            )
    except NotFoundException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=e.msg)


@router.get("/pets/{nome_pet}", tags=["adocoes"])
async def admin_list_adoptions_by_pet(nome_pet: str, admin: str = Depends(validate_admin)):
    try:
        if admin:
            return await get_all_adoptions_by_pet(
                nome_pet,
                skip=0,
                limit=10
            )
    except NotFoundException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=e.msg)


@router.patch("/{email}/{nome_pet}", tags=["adocoes"])
async def admin_update_adoption_status(email: str, nome_pet: str,
                                       status: StatusAdocaoSchema,
                                       admin: str = Depends(validate_admin)):
    try:
        if admin:
            return await update_request_status(
                email,
                nome_pet,
                status
            )
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=e.msg)