from fastapi.encoders import jsonable_encoder
from bson import ObjectId
from bson import json_util
import json

from src.utils.custom_exceptions import NotInsertedException

async def get_adopter_by_email(adopters_collection, email):
    adopter = await adopters_collection.find_one({'email': email})
    if adopter:
        return json.loads(json_util.dumps(adopter))
    return None
    
    
async def get_adopter_by_id(adopters_collection, id):
    adopter = await adopters_collection.find_one({'_id': ObjectId(id)})
    if adopter:
        return json.loads(json_util.dumps(adopter))
    return None
    
    
async def insert_one_adopter(adopters_collection, adopter):
    adopter_data = jsonable_encoder(adopter)
    adopter = await adopters_collection.insert_one(adopter_data)
    if adopter.inserted_id:
        adopter = await get_adopter_by_id(adopters_collection, adopter.inserted_id)
        return adopter
    return None
    

async def get_adopters(adopters_collection, skip, limit):
    adopters_cursor = adopters_collection.find().skip(skip).limit(int(limit))
    adopters = await adopters_cursor.to_list(length=int(limit))
    return json.loads(json_util.dumps(adopters))


async def update_adopter(adopters_collection, email, data):
    adopter = await adopters_collection.update_one(
        {'email': email},
        {'$set': data}
    )
    if adopter.modified_count:
        return True
    return False

    
async def delete_adopter(adopters_collection, email):
    adopter = await adopters_collection.delete_one(
        {'email': email}
    )
    if adopter.deleted_count:
        return True
    return False