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
        
async def user_verification (session : AsyncSession , users_data) :
    
    result = await session.execute(select(User).where(User.username == users_data.username,
                                                      User.password == users_data.password))
    user = result.scalar_one_or_none()
    return {
        "user_id": user.id,
        "username": user.username 
    }