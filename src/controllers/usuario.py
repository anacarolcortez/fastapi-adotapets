from fastapi import HTTPException
from src.services.usuario import get_user_by_email, insert_user_adopter


async def create_user_adopter(user):
    has_user = await get_user_by_email(user.email)
    if has_user is None:
        return await insert_user_adopter(user)
    raise HTTPException(status_code=400, detail="Usuário já estava cadastrado no sistema")