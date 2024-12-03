from datetime import date
from sqlmodel import SQLModel,Field,Relationship
from typing import Optional
from pydantic import BaseModel

# Title,Authors,Description,Category,Publisher,Price Starting With ($),Publish Date (Month),Publish Date (Year)

class BookData(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    Title: str
    Authors: str
    Description: Optional[str] = Field(default=None)
    Category : Optional[str] = Field(default=None)
    Publisher: Optional[str] = Field(default=None)
    Price: int
    Publish_Month:Optional[int] = Field(default=None)
    Publish_Date:Optional[int] = Field(default=None)
    
    
