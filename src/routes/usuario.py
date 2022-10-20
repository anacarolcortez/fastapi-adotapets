from src.controllers.usuario import (
    create_user_adopter,
)

from fastapi import APIRouter
from src.schemas.usuario import UsuarioSchema


router = APIRouter(prefix="/usuarios")


@router.post("/", tags=["usuarios"])
async def register_user_for_adopter(usuario: UsuarioSchema):
    try:
        return await create_user_adopter(
            usuario
        )
    except Exception as e:
        return e