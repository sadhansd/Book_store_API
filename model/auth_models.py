from pydantic import BaseModel
from sqlmodel import SQLModel,Field
from typing import Optional


class CreateUserRequest(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
    
class User(SQLModel, table=True):
    id :  Optional[int] = Field(default=None, primary_key=True)
    username: str
    hashed_password: str