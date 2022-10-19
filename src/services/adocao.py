from bson import ObjectId
from bson import json_util
import json

from src.server.database import db
adoptions_collection = db.adoptions_collection

async def post_adoption_request(adoption_request):
    adoption_data = await adoptions_collection.insert_one(adoption_request)
    if adoption_data.inserted_id:
        adopter = await get_adoption_request_by_id(adoption_data.inserted_id)
        return adopter
    return None


async def get_adoption_request_by_id(id):
    adoption_request = await adoptions_collection.find_one({'_id': ObjectId(id)})
    if adoption_request:
        return json.loads(json_util.dumps(adoption_request))
    return None

    
async def get_adoption_by_email_and_pet(email, pet_name):
    adoption_request = await adoptions_collection.find_one(
        {
            'adotante.email': email, 
            'pet.nome': pet_name
        })
    if adoption_request:
        return json.loads(json_util.dumps(adoption_request))
    return None


async def get_adoption_requests_by_email(email, skip, limit):
    adoption_cursor = adoptions_collection.find(
        { 'adotante.email': email }
    ).skip(skip).limit(int(limit))
    
    adoptions = await adoption_cursor.to_list(length=int(limit))
    return json.loads(json_util.dumps(adoptions))


async def get_adoption_requests_by_pet(pet_name, skip, limit):
    adoption_cursor = adoptions_collection.find(
        { 'pet.nome': pet_name }
    ).skip(skip).limit(int(limit))
    
    adoptions = await adoption_cursor.to_list(length=int(limit))
    return json.loads(json_util.dumps(adoptions))