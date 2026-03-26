from fastapi import FastAPI
from db.create_db import create_tables

app = FastAPI(
    title="To_Do 📝"
)

@app.on_event("startup")
async def on_startup():
    await create_tables()

@app.get("/home/" ,
         summary="Главная страница" ,
         tags=["Home⬆"])
async def home () :
    return {
        "message" : "Главная страница ⬆"
    } 