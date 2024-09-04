from encryption.constants import DB_DEPENDENCY
from encryption.functions import authenticate_user, create_access_token
from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import Annotated
from datetime import timedelta
from schemas.token import Token

token_router = APIRouter()


# FAZ O LOGIN PARA CONSEGUIR O BEARER TOKEN
@token_router.post('/get', response_model=Token)
async def _login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: DB_DEPENDENCY):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate user.')
    
    token = create_access_token(user.username, user.id, timedelta(minutes=17280))

    return {'access_token': token, 'token_type': 'bearer'}
