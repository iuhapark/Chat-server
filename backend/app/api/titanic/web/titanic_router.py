from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Request(BaseModel):
    question: str

class Response(BaseModel):
    answer: str

@router.post("/titanic")
async def titanic(req:Request):
    print("Enter titanic")
    print(req)
    return Response(answer="100명이야")