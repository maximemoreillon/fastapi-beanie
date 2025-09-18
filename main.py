from fastapi import FastAPI
from routes.items import router as itemsRouter
from db import init as init_db

app = FastAPI()

app.include_router(itemsRouter)


@app.on_event("startup")
async def on_startup():
    await init_db()
