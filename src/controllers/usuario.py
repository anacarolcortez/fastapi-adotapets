from src.services.usuario import get_user_by_email, insert_user_adopter
from src.utils.custom_exceptions import NotInsertedException


async def create_user_adopter(user):
    has_user = await get_user_by_email(user.email)
    if has_user is None:
        return await insert_user_adopter(user)
    raise NotInsertedException("Usuário já estava cadastrado no sistema")