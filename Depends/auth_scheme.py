import os
from dotenv import find_dotenv , load_dotenv
from datetime import datetime, timedelta, timezone
from jose import jwt
from fastapi.security import HTTPBearer , HTTPAuthorizationCredentials
from fastapi import Depends

find_dotenv(load_dotenv())

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

secret = HTTPBearer()

def encode_jwt (data : dict) :
    pass