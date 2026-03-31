import os
from dotenv import find_dotenv , load_dotenv
from datetime import datetime, timedelta, timezone
from jose import jwt
from fastapi.security import HTTPBearer , HTTPAuthorizationCredentials
from fastapi import Depends

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

secret = HTTPBearer()

