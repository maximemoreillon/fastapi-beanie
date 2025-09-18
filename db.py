from beanie import init_beanie
from dotenv import load_dotenv
from os import getenv
from models.items import Item

# from pymongo import AsyncMongoClient

load_dotenv()


MONGODB_URL = getenv("MONGODB_URL", "mongodb://localhost:27017/fastapi-beanie-crud")


async def init():

    # client = AsyncMongoClient(
    #     "mongodb://user:pass@host:27017"
    # )

    # await init_beanie(database=client.db_name, document_models=[Item])

    # TODO: figure out if this isn't better
    await init_beanie(connection_string=MONGODB_URL, document_models=[Item])
