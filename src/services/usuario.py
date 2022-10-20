from fastapi.encoders import jsonable_encoder
from bson import ObjectId
from bson import json_util
import json

from src.utils.custom_exceptions import NotInsertedException

from src.server.database import get_collection
users_collection = get_collection("usuarios")


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
    
    
async def insert_user_adopter(user):
    user_data = jsonable_encoder(user)
    user = await users_collection.insert_one(user_data)
    if user.inserted_id:
        user = await get_user_by_id(user.inserted_id)
        return user
    raise NotInsertedException("Erro ao cadastrar usuário")


async def delete_user(email):
    user = await users_collection.delete_one(
        {'email': email}
    )
    if user.deleted_count:
        return True
    return False