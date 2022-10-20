from fastapi.encoders import jsonable_encoder
from bson import ObjectId
from bson import json_util
import json

from src.server.database import get_collection
pets_collection = get_collection("pets")


async def get_pet_by_name(name):
    pet = await pets_collection.find_one({'nome': name})
    if pet:
        return json.loads(json_util.dumps(pet))
    return None
    
    
async def get_pet_by_id(id):
    pet = await pets_collection.find_one({'_id': ObjectId(id)})
    if pet:
        return json.loads(json_util.dumps(pet))
    return None
    
  
async def insert_one_pet(pet):
    pet_data = jsonable_encoder(pet)
    pet = await pets_collection.insert_one(pet_data)
    if pet.inserted_id:
        pet = await get_pet_by_id(pet.inserted_id)
        return pet
    return None
    

async def get_pets_to_adoption(skip, limit):
    pets_cursor = pets_collection.find({'adotado': False}).skip(skip).limit(int(limit))
    pets = await pets_cursor.to_list(length=int(limit))
    return json.loads(json_util.dumps(pets))


async def update_pet(name, data):
    pet = await pets_collection.update_one(
        {'nome': name},
        {'$set': data}
    )
    if pet.modified_count:
        return True
    return False
    

async def delete_pet(name):
    pet = await pets_collection.delete_one(
        {'nome': name}
    )
    if pet.deleted_count:
        return True
    return False


async def update_adopted_status_pet(name, status):
    pet = await pets_collection.update_one(
        {'nome': name},
        {'$set': {'adotado': status["deferido"]}}
    )
    if pet.modified_count:
        return True
    return False