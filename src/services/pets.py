from fastapi.encoders import jsonable_encoder
from bson import ObjectId
from bson import json_util
import json

from src.utils.custom_exceptions import NotFoundException, NotInsertedException, NotUpdatedException

async def get_pet_by_name(pets_collection, name):
    try:
        pet = await pets_collection.find_one({'nome': name})
        if pet:
            return json.loads(json_util.dumps(pet))
    except Exception as e:
        return f"{e}"
    
    
async def get_pet_by_id(pets_collection, id):
    try:
        pet = await pets_collection.find_one({'_id': ObjectId(id)})
        if pet:
            return json.loads(json_util.dumps(pet))
    except Exception as e:
        return f"{e}"
    
    
async def insert_one_pet(pets_collection, pet):
    try:
        pet_data = jsonable_encoder(pet)
        pet = await pets_collection.insert_one(pet_data)
        if pet.inserted_id:
            pet = await get_pet_by_id(pets_collection, pet.inserted_id)
            return pet
        else:
            raise NotInsertedException("Erro ao cadastrar pet")
    except Exception as e:
        return f"{e}"
    

async def get_pets(pets_collection, skip, limit):
    try:
        pets_cursor = pets_collection.find().skip(skip).limit(int(limit))
        pets = await pets_cursor.to_list(length=int(limit))
        return json.loads(json_util.dumps(pets))
    except Exception as e:
        return f'{e}'


async def update_pet(pets_collection, name, data):
    try:
        pet = await pets_collection.update_one(
            {'nome': name},
            {'$set': data}
        )
        return pet.modified_count
    except Exception as e:
        return f'{e}'
    

async def delete_pet(pets_collection, name):
    try:
        pet = await pets_collection.delete_one(
            {'nome': name}
        )
        if pet.deleted_count:
            return True
        return False
    except Exception as e:
        return f'{e}'