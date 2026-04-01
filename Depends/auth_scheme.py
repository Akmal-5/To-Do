import os
from dotenv import find_dotenv , load_dotenv
from datetime import datetime, timedelta, timezone
from jose import jwt , JWTError , ExpiredSignatureError
from fastapi.security import HTTPBearer , HTTPAuthorizationCredentials
from fastapi import Depends , HTTPException ,  status
from typing import Annotated

load_dotenv(find_dotenv())

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

secret = HTTPBearer()

def encode_jwt (users_data : dict) :
    
    data_copy = users_data.copy()
    
    now = datetime.now(timezone.utc)
    
    expire = now + timedelta(minutes=60)
    
    data_copy.update({"exp" : expire})
    
    encode = jwt.encode(data_copy , SECRET_KEY , algorithm=ALGORITHM)
    
    return  encode

#Декодируем наш JWT для получение его данных
def decode_jwt (auth : Annotated[HTTPAuthorizationCredentials , Depends(secret)]) :
 
    token = auth.credentials
 
    try :
        
        token_decode = jwt.decode(token ,  SECRET_KEY , [ALGORITHM])
        user_id = token_decode.get("user_id")
        return user_id
    
    except ExpiredSignatureError :
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Token expired")
        
    except JWTError :
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )