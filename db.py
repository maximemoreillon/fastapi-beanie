from beanie import init_beanie
from dotenv import load_dotenv
from os import getenv
from pymongo import AsyncMongoClient
from models.items import Item

load_dotenv()


MONGODB_URL = getenv("MONGODB_URL", "mongodb://localhost:27017/fastapi-beanie-crud")


async def init():
    client = AsyncMongoClient(MONGODB_URL)

    # Init beanie with the Product document class
    await init_beanie(database=client.db_name, document_models=[Item])
