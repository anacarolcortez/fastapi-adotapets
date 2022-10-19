from fastapi.encoders import jsonable_encoder
from bson import ObjectId
from bson import json_util
import json

from src.utils.custom_exceptions import NotInsertedException

from src.server.database import db
users_collection = db.users_collection


async def get_user_by_email(email):
    user = await users_collection.find_one({'email': email})
    if user:
        return json.loads(json_util.dumps(user))
    return None
    
    
async def get_user_by_id(id):
    user = await users_collection.find_one({'_id': ObjectId(id)})
    if user:
        return json.loads(json_util.dumps(user))
    return None
    
    
async def insert_user_adopter(adopter):
    adopter_data = jsonable_encoder(adopter)
    adopter = await users_collection.insert_one(adopter_data)
    if adopter.inserted_id:
        adopter = await get_user_by_id(adopter.inserted_id)
        return adopter
    raise NotInsertedException("Erro ao cadastrar usuário para o adotante")


async def delete_user(email):
    user = await users_collection.delete_one(
        {'email': email}
    )
    if user.deleted_count:
        return True
    return False