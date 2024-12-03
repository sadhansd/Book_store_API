from fastapi import FastAPI
import uvicorn
from contextlib import asynccontextmanager
from database.database import init_db
from services.service import *
from routes.crud import book_router
from routes.auth import auth

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


if __name__ == "__main__":
    
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)