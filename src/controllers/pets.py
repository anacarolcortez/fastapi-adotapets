from bson import ObjectId
from fastapi.encoders import jsonable_encoder

from src.services.pets import (
    delete_pet,
    get_pet_by_name,
    insert_one_pet,
    get_pets,
    update_pet
)
from src.utils.custom_exceptions import NotFoundException, NotInsertedException, NotUpdatedException


async def find_pet(pets_collection, name):
    try:
        pet = await get_pet_by_name(pets_collection, name)
        if pet is not None:
            return pet
        raise NotFoundException(f"Pet {name} não encontrado no sistema")
    except Exception as e:
        return f'find_pet.error: {e}'


async def create_pet(pets_collection, pet):
    try:
        has_pet = await get_pet_by_name(pets_collection, pet.nome)
        if has_pet is None:
            return await insert_one_pet(pets_collection, pet)
        raise NotInsertedException("Pet já cadastrado no sistema")
    except Exception as e:
        return f'create_pet.error: {e}'


async def get_all_pets(pets_collection, skip, limit):
    try:
        return await get_pets(pets_collection, int(skip), int(limit))
    except Exception as e:
        return f'get_all_pets.error: {e}'


async def update_pet_info(pets_collection, name, data):
    try:
        pet = await get_pet_by_name(pets_collection, name)
        if pet is not None:
            data_dict = jsonable_encoder(data)
            updated_count = await update_pet(pets_collection, name, data_dict)
            if updated_count:
                return await get_pet_by_name(pets_collection, name)
        raise NotUpdatedException("Erro ao atualizar cadastro do pet")
    except Exception as e:
        return f'update_pet_info.error: {e}'
    
    
async def delete_pet_info(pets_collection, name):
    try:
        pet = await get_pet_by_name(pets_collection, name)
        if pet is not None:
            response = await delete_pet(pets_collection, name)
            if response:
                return f'Pet {name} removido do banco de dados'
        raise NotFoundException("Erro ao remover cadastro; pet não encontrado")
    except Exception as e:
        return f'delete_pet_info.error: {e}'