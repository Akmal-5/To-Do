from db.config import AsyncSessionMaker


async def get_session () :
    async with AsyncSessionMaker() as session :
        yield session