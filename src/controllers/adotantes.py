from datetime import datetime
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from src.schemas.adotante import AdotanteSchema
from src.schemas.usuario import UsuarioSchema

from src.services.adotante import (
    delete_adopter,
    get_adopter_by_email,
    get_adopters,
    insert_one_adopter,
    update_adopter
)
from src.services.usuario import delete_user, get_user_by_email, insert_user_adopter


async def find_adopter(adopters_collection, email):
    adopter = await get_adopter_by_email(adopters_collection, email)
    if adopter is not None:
        return adopter
    raise HTTPException(status_code=404, detail="Adotante não encontrado no sistema")


async def create_adopter(adopters_collection, users_collection, adopter):
    has_adopter = await get_adopter_by_email(adopters_collection, adopter.email)
    has_user = await get_user_by_email(users_collection, adopter.email)
    if has_adopter is None and has_user is None:
        user_adopter = await get_object_user(adopter)
        person_adopter = await get_object_adopter(adopter)
        await insert_user_adopter(users_collection, user_adopter)
        return await insert_one_adopter(adopters_collection, person_adopter)
    raise HTTPException(status_code=400, detail="Adotante já estava cadastrado no sistema")


async def get_all_adopters(adopters_collection, skip, limit):
    try:
        return await get_adopters(adopters_collection, int(skip), int(limit))
    except Exception:
        raise HTTPException(status_code=404, detail="Erro na listagem de adotantes do sistema")


async def update_adopter_info(adopters_collection, name, data):
    adopter = await get_adopter_by_email(adopters_collection, name)
    if adopter is not None:
        data_dict = jsonable_encoder(data)
        updated_count = await update_adopter(adopters_collection, name, data_dict)
        if updated_count:
            return await get_adopter_by_email(adopters_collection, name)
    raise HTTPException(status_code=400, detail="Erro ao atualizar cadastro: adotante não encontrado no sistema")
    
    
async def delete_adopter_info(adopters_collection, users_collection, email):
    adopter = await get_adopter_by_email(adopters_collection, email)
    user = await get_user_by_email(users_collection, email)
    if adopter is not None and user is not None:
        response_adopter = await delete_adopter(adopters_collection, email)
        response_user = await delete_user(users_collection, email)
        if response_adopter and response_user:
            return {
                "status_code": 200,
                "detail": "Adotante e respectivo usuário foram removidos do sistema",
                "headers": None
                }
    raise HTTPException(status_code=400, detail="Erro ao excluir cadastro: usuário ou adotante não encontrado no sistema")


async def get_object_user(adopter):
    user = UsuarioSchema(
        email=adopter.email,
        senha=adopter.senha,
    )
    return user

async def get_object_adopter(adopter):
    person = AdotanteSchema(
        nome=adopter.nome,
        cpf=adopter.cpf,
        email=adopter.email,
        telefone=adopter.telefone,
        data_nasc=adopter.data_nasc,
        sexo=adopter.sexo,
        data_cadastro=datetime.now(),
        obs=adopter.obs
    )
    return person