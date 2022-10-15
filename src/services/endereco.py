from fastapi.encoders import jsonable_encoder
from bson import ObjectId
from bson import json_util
import json

async def create_client_address(address_collection, address, email):
    address_data = jsonable_encoder(address)
    created_address = await address_collection.insert_one(
        { 
         "adotante": email, 
         "endereco": address_data 
        })
    if created_address.inserted_id:
        response = await get_address_by_id(address_collection, created_address.inserted_id)
        return response
    return None


async def get_address_by_id(address_collection, id):
    inserted_address = await address_collection.find_one({"_id": ObjectId(id)})
    if inserted_address is not None:
        return json.loads(json_util.dumps(inserted_address))
    return None


async def get_address_by_adopter_email(address_collection, email):
    address = await address_collection.find_one({"adotante": email})
    if address is not None:
        return json.loads(json_util.dumps(address))
    return None