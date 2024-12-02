from fastapi import FastAPI,APIRouter
import uvicorn
from contextlib import asynccontextmanager
from database.database import init_db,get_session
from sqlmodel import Session,select
from model.models import BookData
from services.service import *
from routes.crud import book_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(book_router, prefix="/book")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")