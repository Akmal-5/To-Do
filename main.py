from fastapi import FastAPI , Depends , status , HTTPException , Query
from db.create_db import create_tables
from models.models_data import User , UserLog , UserTasks
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from db.data_manipulation import (create_user , 
                                  user_verification,
                                  create_user_task,
                                  get_users_task
                                  )
from Depends.create_session import get_session
from Depends.auth_scheme import encode_jwt , decode_jwt
from fastapi.security import HTTPAuthorizationCredentials

app = FastAPI(
    title="To Do project📝"
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
async def user_login (userlog : UserLog ,
                      session : Annotated[AsyncSession , Depends(get_session)]) :
    
    result = await user_verification(session , userlog)
    
    if result :
        res = encode_jwt(result)
        return {
            "token" : res  
        }
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail="Incorrect data or you are not registered")

@app.post("/tasks/" ,
          summary="Добавить задачу",
          tags=["Tasks📝"],
          status_code=status.HTTP_201_CREATED
          )
async def create_tasks (usertasks : UserTasks ,
                        user_id : Annotated[int , Depends(decode_jwt)],
                        session : Annotated[AsyncSession , Depends(get_session)],                       
                        ) :
    result = await create_user_task(session  , user_id , usertasks)
    
    await session.commit()
    
    return result

@app.get("/tasks/" ,
        summary="Получить задачу",
        tags=["Tasks📝"]
        )
async def get_task (session : Annotated[AsyncSession , Depends(get_session)],
                    user_id : Annotated[int , Depends(decode_jwt)],
                    filtering_by_title : Annotated[str | None, Query()] = None) :
    
    return await get_users_task(session , user_id , filtering_by_title)