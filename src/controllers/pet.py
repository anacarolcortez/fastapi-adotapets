from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException

from src.services.pet import (
    delete_pet,
    get_pet_by_name,
    insert_one_pet,
    get_pets,
    update_pet
)


async def find_pet(name):
    pet = await get_pet_by_name(name)
    if pet is not None:
        return pet
    raise HTTPException(status_code=404, detail="Pet não encontrado no sistema")


async def create_pet(pet):
    has_pet = await get_pet_by_name(pet.nome)
    if has_pet is None:
        return await insert_one_pet(pet)
    raise HTTPException(status_code=400, detail="Pet já estava cadastrado no sistema")


async def get_all_pets(skip, limit):
    try:
        return await get_pets(int(skip), int(limit))
    except Exception as e:
        raise HTTPException(status_code=400, detail="Erro ao retornar lista de pets cadastrados")


async def update_pet_info(name, data):
    pet = await get_pet_by_name(name)
    if pet is not None:
        data_dict = jsonable_encoder(data)
        updated_count = await update_pet(name, data_dict)
        if updated_count:
            return await get_pet_by_name(name)
    raise HTTPException(status_code=404, detail="Erro ao atualizar cadastro: pet não encontrado no sistema")
    
    
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
    raise HTTPException(status_code=404, detail="Erro ao excluir cadastro: pet não encontrado no sistema")
