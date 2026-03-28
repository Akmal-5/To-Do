#Создание удоление то есть манипуляция данными
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from db.User import User

async def create_user (session : AsyncSession , user_data) :
    
    result  = await session.execute(select(User).where(User.username == user_data.username, 
                                       User.password == user_data.password))
    
    user = result.scalar_one_or_none()
    
    if not user :
        
        session.add(User(
            
            username = user_data.username,
            password = user_data.password,
            email = user_data.email   
        ))
        
        return {
            "message" : "Добавил в бд"
        }