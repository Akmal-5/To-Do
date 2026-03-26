from db.config import Base , engine

async def create_tables():
        async with engine.begin() as con :
                await con.run_sync(Base.metadata.create_all)