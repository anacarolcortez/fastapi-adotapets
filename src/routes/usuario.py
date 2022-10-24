from fastapi import APIRouter, HTTPException, status
from src.controllers.usuario import (
    create_user_adopter,
)
from src.schemas.usuario import UsuarioSchema
from src.utils.custom_exceptions import NotInsertedException


router = APIRouter(prefix="/usuarios")


@router.post("/", status_code=status.HTTP_201_CREATED, tags=["usuarios"])
async def register_user_for_adopter(usuario: UsuarioSchema):
    try:
        return await create_user_adopter(
            usuario
        )
    except NotInsertedException as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
        detail=e.msg)