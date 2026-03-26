import os
from dotenv import find_dotenv , load_dotenv
from sqlalchemy.ext.asyncio import  create_async_engine , AsyncSession
from sqlalchemy.orm import DeclarativeBase , sessionmaker

load_dotenv(find_dotenv())

PASSWORD = os.getenv("PASSWORD")
DATABASE = os.getenv("DATABASE")

engine = create_async_engine (
        
    url = f"mysql+asyncmy://root:{PASSWORD}@localhost:3306/{DATABASE}",
    echo = False
)

AsyncSessionMaker = sessionmaker(
    engine,
    class_=AsyncSession,   
)

class Base (DeclarativeBase) :
    pass