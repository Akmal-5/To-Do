from db.config import AsyncSessionMaker


#Для создание сессий
async def get_session () :
    async with AsyncSessionMaker() as session :
        yield session
