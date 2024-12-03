from fastapi import Request, HTTPException,status
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Any,Callable

class ErrorResponse(BaseModel):
    message: str
    status_code: str

class InvalidIDError(Exception):
    def __init__(self,**kwargs):
        self.detail = kwargs.get('detail',"Invalid ID")
        self.status_code = status.HTTP_404_NOT_FOUND
        
async def Invalid_exception_handler(request: Request, exc: InvalidIDError):
    return JSONResponse(
        status_code=exc.status_code,
        content=ErrorResponse(
            message=str(exc.detail), 
            status_code=str(exc.status_code)).model_dump()
    )
