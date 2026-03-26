from db.config import Base
from sqlalchemy import String , ForeignKey
from sqlalchemy.orm import Mapped ,  mapped_column

class User (Base) :
    
    __tablename__ = "users"
    id : Mapped[int] = mapped_column(primary_key=True)
    username : Mapped[str] = mapped_column(String(70))
    password : Mapped[str] = mapped_column(String(100))
    email  : Mapped[str] = mapped_column(String(200))
    

class UsersNote(Base) :
    
    __tablename__ = "users_note"
    id : Mapped[int] = mapped_column(primary_key=True)
    user_id : Mapped[int] = mapped_column(ForeignKey("users.id"))
    title : Mapped[str] = mapped_column(String(200) ,
                                        nullable=False)    
    description : Mapped[str] = mapped_column(String(300))