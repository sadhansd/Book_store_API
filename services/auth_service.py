from fastapi import Depends, HTTPException, status,APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from typing import Annotated
from database.database import get_session
from sqlmodel import Session,select
from model.auth_models import *

db = Annotated[Session, Depends(get_session)]

SECRET_KEY = "93E396EF02D176C0700F50A60EB529AB "
ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")


def register_user(session: db, create_user_request: User):
    create_user_model = User(username=create_user_request.username, hashed_password=pwd_context.hash(create_user_request.password))
    session.add(create_user_model)
    session.commit()
    
def get_access_token(session: db, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = authenticate(session, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    token = create_access_token(user.username, user.id, timedelta(minutes=30))
    return token

def authenticate(session: db, username: str, password: str):
    user = session.exec(select(User).where(User.username == username)).first()
    if not user:
        return False
    if not pwd_context.verify(password, user.hashed_password):
        return False
    return user

def create_access_token(username: str, user_id: int, expire: timedelta):
    encode = {'sub': username, 'id':user_id }
    expire = datetime.now() + expire
    encode.update({'exp': expire})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        user_id: int = payload.get('id')
        
        return {'username': username, 'user_id':user_id}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)