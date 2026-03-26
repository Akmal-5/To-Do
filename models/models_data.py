from pydantic import BaseModel , Field , EmailStr

class User (BaseModel) :
    username : str = Field(min_length=3 ,
                           description="Имя пользователя")
    password : str = Field(min_length=4 ,
                           description="Пароль пользователя")
    
    email : EmailStr = Field(
        description="Почта пользователя"
    )

class UsersNote (BaseModel) :
    
    title : str 
    description : int | None = Field(
        default=None
    )