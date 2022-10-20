import asyncio
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase, AsyncIOMotorCollection
from os import environ
from dotenv import load_dotenv
load_dotenv()


def config_db():
    client = AsyncIOMotorClient(environ.get("KEY"))
    client.get_io_loop = asyncio.get_event_loop
    return client


def get_db() -> AsyncIOMotorDatabase:
    db = config_db()
    return db["adotapets"]

    
def get_collection(name: str) -> AsyncIOMotorCollection:
    db = get_db()
    collection = db[name]
    return collection