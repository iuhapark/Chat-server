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
    hello = '/Users/juhapark/IdeaProjects/Kubernetes/chat-server/backend/app/api/titanic/data/hello.txt'
    
    return Response(answer="생존자는 100명이야")