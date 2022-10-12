from fastapi.encoders import jsonable_encoder
from bson import ObjectId
from bson import json_util
import json

from src.utils.custom_exceptions import NotInsertedException

async def get_adopter_by_email(adopters_collection, email):
    try:
        adopter = await adopters_collection.find_one({'email': email})
        if adopter:
            return json.loads(json_util.dumps(adopter))
    except Exception as e:
        return f"{e}"
    
    
async def get_adopter_by_id(adopters_collection, id):
    try:
        adopter = await adopters_collection.find_one({'_id': ObjectId(id)})
        if adopter:
            return json.loads(json_util.dumps(adopter))
    except Exception as e:
        return f"{e}"
    
    
async def insert_one_adopter(adopters_collection, adopter):
    try:
        adopter_data = jsonable_encoder(adopter)
        adopter = await adopters_collection.insert_one(adopter_data)
        if adopter.inserted_id:
            adopter = await get_adopter_by_id(adopters_collection, adopter.inserted_id)
            return adopter
        else:
            raise NotInsertedException("Erro ao cadastrar adotante")
    except Exception as e:
        return f"{e}"
    

async def get_adopters(adopters_collection, skip, limit):
    try:
        adopters_cursor = adopters_collection.find().skip(skip).limit(int(limit))
        adopters = await adopters_cursor.to_list(length=int(limit))
        return json.loads(json_util.dumps(adopters))
    except Exception as e:
        return f'{e}'


async def update_adopter(adopters_collection, email, data):
    try:
        adopter = await adopters_collection.update_one(
            {'email': email},
            {'$set': data}
        )
        return adopter.modified_count
    except Exception as e:
        return f'{e}'
    

async def delete_adopter(adopters_collection, email):
    try:
        adopter = await adopters_collection.delete_one(
            {'email': email}
        )
        if adopter.deleted_count:
            return True
        return False
    except Exception as e:
        return f'{e}'