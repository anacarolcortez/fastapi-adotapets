from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException

from src.services.pet import (
    delete_pet,
    get_pet_by_name,
    get_pets_to_adoption,
    insert_one_pet,
    update_pet
)
from src.utils.custom_exceptions import NotDeletedException, NotFoundException, NotInsertedException, NotUpdatedException


async def find_pet(name):
    pet = await get_pet_by_name(name)
    if pet is not None:
        return pet
    raise NotFoundException("Pet não encontrado no sistema")


async def create_pet(pet):
    has_pet = await get_pet_by_name(pet.nome)
    if has_pet is None:
        return await insert_one_pet(pet)
    raise NotInsertedException("Pet já estava cadastrado no sistema")


async def get_all_pets(skip, limit):
    try:
        return await get_pets_to_adoption(int(skip), int(limit))
    except Exception as e:
        raise NotFoundException("Erro ao retornar lista de pets cadastrados")


async def update_pet_info(name, data):
    pet = await get_pet_by_name(name)
    if pet is not None:
        data_dict = jsonable_encoder(data)
        updated_count = await update_pet(name, data_dict)
        if updated_count:
            return await get_pet_by_name(name)
    raise NotUpdatedException("Erro ao atualizar cadastro: pet não encontrado no sistema")
    
    
async def delete_pet_info(name):
    pet = await get_pet_by_name(name)
    if pet is not None:
        response = await delete_pet(name)
        if response:
            return {
                "status_code": 200,
                "detail": "Pet removido do sistema",
                "headers": None
                }
    raise NotDeletedException("Erro ao excluir cadastro: pet não encontrado no sistema")
