from fastapi import Depends, HTTPException, status,APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from typing import Annotated
from database.database import get_session
from sqlmodel import Session,select
from model.auth_models import *
from services.auth_service import *

db = Annotated[Session, Depends(get_session)]

auth = APIRouter(
    prefix='/auth',tags=['auth']
)

@auth.post("/register", status_code=status.HTTP_201_CREATED)
async def create_user(session: db, create_user_request: CreateUserRequest):
    user = register_user(session, create_user_request)
    return {"Message": "User registered successfully"}

@auth.post("/token", response_model=Token)
async def login_for_access_token(session: db, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    token = get_access_token(session, form_data)
    return {'access_token': token, "token_type":'bearer'}
    
user_dependency = Annotated[dict, Depends(get_current_user)]

@auth.get('/')
async def user(user: user_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid User")
    return{'user': user}

@auth.get('/allUsers')
def get_AllUsers(session: Annotated[Session, Depends(get_session)]):
    return session.exec(select(User)).all()