from bson import ObjectId
from bson import json_util
import json

from src.server.database import db
address_collection = db.address_collection

async def create_client_address(address, email):
    created_address = await address_collection.insert_one(
        { 
         "adotante": email, 
         "endereco": address
        })
    if created_address.inserted_id:
        response = await get_address_by_id(created_address.inserted_id)
        return response
    return None


async def get_address_by_id(id):
    inserted_address = await address_collection.find_one({"_id": ObjectId(id)})
    if inserted_address is not None:
        return json.loads(json_util.dumps(inserted_address))
    return None


async def get_address_by_adopter_email(email):
    address = await address_collection.find_one({"adotante": email})
    if address is not None:
        return json.loads(json_util.dumps(address))
    return None


async def update_address_by_email(address, email):
    updated_address = await address_collection.update_one(
        {'adotante': email},
        {'$set': {'endereco': address}}
    )
    if updated_address.modified_count:
        return True
    return False


async def delete_address_by_email(email):
    address = await address_collection.delete_one(
        {'adotante': email}
    )
    if address.deleted_count:
        return True
    return False