from fastapi import FastAPI

from app.database import init_db
from app.models import Product

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    await init_db()


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}
