from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException

from src.services.pets import (
    delete_pet,
    get_pet_by_name,
    insert_one_pet,
    get_pets,
    update_pet
)
from src.utils.custom_exceptions import NotFoundException, NotInsertedException, NotUpdatedException


async def find_pet(pets_collection, name):
    pet = await get_pet_by_name(pets_collection, name)
    if pet is not None:
        return pet
    raise HTTPException(status_code=404, detail="Pet não encontrado no sistema")


async def create_pet(pets_collection, pet):
    has_pet = await get_pet_by_name(pets_collection, pet.nome)
    if has_pet is None:
        return await insert_one_pet(pets_collection, pet)
    raise HTTPException(status_code=400, detail="Pet já estava cadastrado no sistema")


async def get_all_pets(pets_collection, skip, limit):
    try:
        return await get_pets(pets_collection, int(skip), int(limit))
    except Exception as e:
        raise HTTPException(status_code=400, detail="Erro ao retornar lista de pets cadastrados")


async def update_pet_info(pets_collection, name, data):
    pet = await get_pet_by_name(pets_collection, name)
    if pet is not None:
        data_dict = jsonable_encoder(data)
        updated_count = await update_pet(pets_collection, name, data_dict)
        if updated_count:
            return await get_pet_by_name(pets_collection, name)
    raise HTTPException(status_code=404, detail="Erro ao atualizar cadastro: pet não encontrado no sistema")
    
    
async def delete_pet_info(pets_collection, name):
    pet = await get_pet_by_name(pets_collection, name)
    if pet is not None:
        response = await delete_pet(pets_collection, name)
        if response:
            return {
                "status_code": 200,
                "detail": "Pet removido do sistema",
                "headers": None
                }
    raise HTTPException(status_code=404, detail="Erro ao excluir cadastro: pet não encontrado no sistema")
