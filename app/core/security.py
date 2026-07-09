from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordBearer
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
import bcrypt

from app.core.config import SECRET_KEY

# pwd_context = CryptContext(schemes=["bcrypt_sha256"], deprecated="auto")

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 15
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def hash_password(password):
    pw_byte = password.encode("utf-8")
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(pw_byte,salt=salt).decode()

def verify_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode(), hashed_password.encode())

def generate_access_token(userData: dict):
    to_encode = userData.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    return jwt.encode(to_encode,f"{SECRET_KEY}", algorithm=ALGORITHM)

def verify_access_token(token: str):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail={"error": "could not validate credentials"}, headers={"WWW-Authenticate": "Bearer"})
    try:
        payload = jwt.decode(token=token,key=f"{SECRET_KEY}", algorithms=[ALGORITHM])
    except JWTError:
        raise credentials_exception
    
    return payload

def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = verify_access_token(token)
    user_id = payload.get("user_id")
    return user_id
