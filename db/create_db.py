from db.config import Base , engine
from db.User import User 
from db.UsersNote import UsersNote

async def create_tables():
        async with engine.begin() as con :
                await con.run_sync(Base.metadata.create_all)