from fastapi import FastAPI , Depends , status , HTTPException
from db.create_db import create_tables
from models.models_data import User
from db.config import AsyncSessionMaker
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from db.data_manipulation import (create_user)
from Depends.depends import get_session

app = FastAPI(
    title="To_Do 📝"
)

#Устаревший способ !
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
    
@app.post("/auth/register/" ,
          summary="Регистрация ✅",
          tags=["Users🙍‍♂️"] ,
          status_code=status.HTTP_201_CREATED)

async def user_register (user : User , 
                         session : Annotated[AsyncSession , Depends(get_session)] ,
                         ) :
    result = await create_user(session , user)
    
    if result :
        
        await session.commit()
        
        return result
    
    raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                        detail= "This user already exists in the database.")

@app.post("/auth/login" , summary="Авторизация🔐" , tags=["Users🙍‍♂️"])
async def user_login () :
    pass