from fastapi import APIRouter
from models.items import Item

router = APIRouter(prefix="/items")


@router.get("/")
async def handler():
    items = await Item.find_all().to_list()
    return {"items": items}


@router.post("/")
async def handler(item: Item):
    await item.insert()
    return "OK"
