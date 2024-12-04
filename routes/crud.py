from fastapi import FastAPI,HTTPException,APIRouter,Query
from services.service import *
from model.models import BookData,Book

from error.error_handler import InvalidIDError

book_router = APIRouter()

@book_router.get("")
def get_data():
    records = get_all()
    return records

@book_router.get("/{book_id}", response_model=Book)
def get_data(book_id: int):
    records = get_book_id(book_id)
    return records

@book_router.post("/add")
def create_data(book: BookData):
    return add_book(book)

@book_router.delete("/delete/{book_id}")
def delete_data(book_id: int):
    delete_book(book_id)
    return {"message": "Book deleted successfully"}

@book_router.put("/update/{book_id}")
def update_data(book_id: int, updated_data: BookData):
    record = update_book(book_id,updated_data)
    return record
