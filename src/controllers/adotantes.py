from datetime import date, datetime
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
from src.services.usuario import get_user_by_email, insert_user_adopter
from src.utils.custom_exceptions import NotFoundException, NotInsertedException, NotUpdatedException


async def find_adopter(adopters_collection, email):
    try:
        adopter = await get_adopter_by_email(adopters_collection, email)
        if adopter is not None:
            return adopter
        raise NotFoundException(f"Adotante {email} não encontrado no sistema")
    except Exception as e:
        return f'find_adopter.error: {e}'


async def create_adopter(adopters_collection, users_collection, adopter):
    try:
        has_adopter = await get_adopter_by_email(adopters_collection, adopter.email)
        has_user = await get_user_by_email(users_collection, adopter.email)
        if has_adopter is None and has_user is None:
            user_adopter = await get_object_user(adopter)
            person_adopter = await get_object_adopter(adopter)
            await insert_user_adopter(users_collection, user_adopter)
            return await insert_one_adopter(adopters_collection, person_adopter)
        raise NotInsertedException("Adotante já cadastrado no sistema")
    except Exception as e:
        return f'create_adopter.error: {e}'


async def get_all_adopters(adopters_collection, skip, limit):
    try:
        return await get_adopters(adopters_collection, int(skip), int(limit))
    except Exception as e:
        return f'get_all_adopters.error: {e}'


async def update_adopter_info(adopters_collection, name, data):
    try:
        adopter = await get_adopter_by_email(adopters_collection, name)
        if adopter is not None:
            data_dict = jsonable_encoder(data)
            updated_count = await update_adopter(adopters_collection, name, data_dict)
            if updated_count:
                return await get_adopter_by_email(adopters_collection, name)
        raise NotUpdatedException("Erro ao atualizar cadastro do adotante")
    except Exception as e:
        return f'update_adopter_info.error: {e}'
    
    
async def delete_adopter_info(adopters_collection, email):
    try:
        pet = await get_adopter_by_email(adopters_collection, email)
        if pet is not None:
            response = await delete_adopter(adopters_collection, email)
            if response:
                return f'Adotante {email} removido do banco de dados'
        raise NotFoundException("Erro ao remover cadastro; adotante não encontrado")
    except Exception as e:
        return f'delete_adopter_info.error: {e}'
    
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