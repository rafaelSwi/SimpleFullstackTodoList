from datetime import timedelta, datetime
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from passlib.context import CryptContext
from typing import Annotated
from jose import jwt, JWTError
import models as mo

def get_bcrypt_context():
    return CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_oauth_bearer():
    return OAuth2PasswordBearer(tokenUrl='auth/token')

def get_secret_key() -> str:
    return "Ufn4kd7dj0aLkduT653hGidj"

def get_algorithm() -> str:
    return "HS256"

async def get_current_user(token: Annotated[str, Depends(get_oauth_bearer())]):
    try:
        payload = jwt.decode(token, get_secret_key(), algorithms=[get_algorithm()])
        username: str = payload.get('sub')
        user_id: int = payload.get('id')
        if username is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate user.')
        return {'username': username, 'id': user_id}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate user.')

def get_password_hash(password: str) -> str:
    return get_bcrypt_context().hash(password)

def authenticate_user(username: str, password: str, db):
    user = db.query(mo.Cadastro).filter(mo.Cadastro.username == username).first()
    if not user:
        return False
    if not get_bcrypt_context().verify(password, user.password_hash):
        return False
    return user

def create_access_token(username: str, user_id: str, expires_delta: timedelta):
    encode = {'sub': username, 'id': user_id}
    expires = datetime.utcnow() + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode, get_secret_key(), algorithm=get_algorithm())