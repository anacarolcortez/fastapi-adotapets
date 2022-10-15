from bson import ObjectId
from bson import json_util
import json


async def post_adoption_request(adoptions_collection, adoption_request):
    adoption_data = await adoptions_collection.insert_one(adoption_request)
    if adoption_data.inserted_id:
        adopter = await get_adoption_request_by_id(adoptions_collection, adoption_data.inserted_id)
        return adopter
    return None


async def get_adoption_request_by_id(adoptions_collection, id):
    adoption_request = await adoptions_collection.find_one({'_id': ObjectId(id)})
    if adoption_request:
        return json.loads(json_util.dumps(adoption_request))
    return None

    
async def get_adoption_by_email_and_pet(adoptions_collection, email, pet_name):
    adoption_request = await adoptions_collection.find_one(
        {
            'adotante.email': email, 
            'pet.nome': pet_name
        })
    if adoption_request:
        return json.loads(json_util.dumps(adoption_request))
    return None