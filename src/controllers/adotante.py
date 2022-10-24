from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder


from src.services.adotante import (
    delete_adopter,
    get_adopter_by_email,
    get_adopters,
    insert_one_adopter,
    update_adopter
)
from src.services.usuario import (
    delete_user, 
    get_user_by_email, 
)
from src.utils.custom_exceptions import NotDeletedException, NotFoundException, NotInsertedException, NotUpdatedException

async def find_adopter(email):
    adopter = await get_adopter_by_email(email)
    if adopter is not None:
        return adopter
    raise NotFoundException("Adotante não encontrado no sistema")


async def create_adopter(adopter, email):
    has_adopter = await get_adopter_by_email(email)
    if has_adopter is None:
        person_adopter = await get_object_adopter(adopter, email)
        return await insert_one_adopter(person_adopter)
    raise NotInsertedException("Adotante já estava cadastrado no sistema")


async def get_all_adopters(skip, limit):
    try:
        return await get_adopters(int(skip), int(limit))
    except Exception:
        raise NotFoundException("Erro na listagem de adotantes do sistema")


async def update_adopter_info(name, data):
    adopter = await get_adopter_by_email(name)
    if adopter is not None:
        data_dict = jsonable_encoder(data)
        updated_count = await update_adopter(name, data_dict)
        if updated_count:
            return await get_adopter_by_email(name)
    raise NotUpdatedException("Erro ao atualizar cadastro: adotante não encontrado no sistema")
    
    
async def delete_adopter_info(email):
    adopter = await get_adopter_by_email(email)
    user = await get_user_by_email(email)
    if adopter is not None and user is not None:
        response_adopter = await delete_adopter(email)
        response_user = await delete_user(email)
        if response_adopter and response_user:
            return {
                "status_code": 200,
                "detail": "Adotante e respectivo usuário foram removidos do sistema",
                "headers": None
                }
    raise NotDeletedException("Erro ao excluir cadastro: usuário ou adotante não encontrado no sistema")


async def get_object_adopter(adopter, email):
    person = {
        "email": email,
        "nome": adopter.nome,
        "cpf":adopter.cpf,
        "telefone":adopter.telefone,
        "data_nasc":adopter.data_nasc,
        "sexo": adopter.sexo,
        "endereco": adopter.endereco,
        "data_cadastro": adopter.data_cadastro,
        "obs": adopter.obs
    }
    return person