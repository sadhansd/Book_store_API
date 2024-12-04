from fastapi import FastAPI,status
import uvicorn
from contextlib import asynccontextmanager
from database.database import init_db
from services.service import *
from routes.crud import book_router
from routes.auth import auth
from error.error_handler import InvalidIDError,Invalid_exception_handler
from model.models import *

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

version = "v1"

app = FastAPI(
    lifespan=lifespan,
    title="The books API",  
    version=version
)

app.include_router(book_router, prefix="/book")
app.include_router(auth)

app.add_exception_handler(
    InvalidIDError,
    Invalid_exception_handler
)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)