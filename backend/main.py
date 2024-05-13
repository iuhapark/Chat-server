from fastapi import FastAPI
from langchain.chat_models.openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage
import os
from dotenv import load_dotenv
import uvicorn
from app.api.titanic.model.titanic_model import TitanicModel
from app.main_router import router

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

from pydantic import BaseModel

from starlette.middleware.cors import CORSMiddleware

class Request(BaseModel):
    question: str

class Response(BaseModel):
    answer: str

app = FastAPI()

app.include_router(router, prefix="/api")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


# @app.post("/titanic")
def chatting(req:Request): #타입이 뒤에 있음
    print("딕셔너리 내용")
    print(req)

    chat = ChatOpenAI(
        openai_api_key=os.environ["API_KEY"],
        temperature=0.1,
        max_tokens=2048,
        model_name="gpt-3.5-turbo-0613",
    )

    return Response(answer=chat.predict(req.question))

    # print(f'{chat.predict(req.question)}')

    # message = [
    #     SystemMessage(content="""
    #                   You are a traveler. I know the capitals of all countries in the world.
    #                   """, type="system"),
    #     HumanMessage(content="대한민국의 수도는 어디야?", type="human"),
    #     AIMessage(content="서울입니다..", type="ai"),
    # ]

    # message = [
    #     SystemMessage(content="""
    #                   You are a SQL developer. My database is innodb MySQL."
    #                   +"The database has users and players table. The table has id, name, age columns"+
    #                   "The players table has id, team, back_number columns.
    #                   """, type="system"),
    #     HumanMessage(content="What is the SQL query to get the names of all players?", type="human"),
    #     AIMessage(content="SELECT name FROM players", type="ai"),
    # ]

    # print(chat.predict_messages(message))

    return Response(answer=chat.predict(req.question))

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)