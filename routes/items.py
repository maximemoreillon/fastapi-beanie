from fastapi import APIRouter, HTTPException
from models.items import Item

router = APIRouter(prefix="/items")


@router.post("/")
async def handler(item: Item):
    await item.insert()
    return "OK"


@router.get("/")
async def handler():
    items = await Item.find_all().to_list()
    return {"items": items}


@router.get("/{item_id}")
async def handler(item_id: str):
    item = await Item.get(item_id)
    return item


@router.patch("/{item_id}")
async def handler(item_id: str, new_properties: Item):
    item = await Item.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    await item.set(new_properties.model_dump(exclude_unset=True))
    return item


@router.delete("/{item_id}")
async def handler(item_id: str):
    item = await Item.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    await item.delete()
    return {"item_id": item_id}
