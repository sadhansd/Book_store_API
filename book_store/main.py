from fastapi import FastAPI,Depends
from contextlib import asynccontextmanager
from database import init_db,get_session
from sqlmodel import Session,select
from models import BookData
from service import *

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
def welcome():
    return {"message":"hello"} 

@app.get("/book")
def get_data():
    records = get_all()
    return records

@app.get("/book/{book_id}")
def get_data(book_id: int):
    records = get_book_id(book_id)
    return records

@app.post("/addBook")
def create_data(book: BookData):
    return add_book(book)

@app.delete("/delete/{book_id}")
def delete_data(book_id: int):
    delete_book(book_id)
    return {"message": "Book deleted successfully"}

@app.put("/update/{book_id}")
def update_data(book_id: int, updated_data: BookData):
    record = update_book(book_id,updated_data)
    return record