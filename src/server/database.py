from motor.motor_asyncio import AsyncIOMotorClient
from os import environ
from dotenv import load_dotenv
load_dotenv()


class DataBase():
    client = AsyncIOMotorClient(environ.get("KEY"))
    db = client['adotapets']

    pets_collection = db['pets']
    adopters_collection = db['adotantes']
    adoptions_collection = db['adocoes']
    users_collection = db['usuarios']


db = DataBase()