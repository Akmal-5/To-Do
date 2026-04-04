from db.config import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped ,  mapped_column

class User (Base) :
    
    __tablename__ = "users"
    id : Mapped[int] = mapped_column(primary_key=True)
    username : Mapped[str] = mapped_column(String(70))
    password : Mapped[str] = mapped_column(String(100))
    email  : Mapped[str] = mapped_column(String(200))
    
    def __str__(self):
        
        return f"Id пользователя : {self.id}\nИмя пользователя : {self.username}\nemail пользователя : {self.email}"