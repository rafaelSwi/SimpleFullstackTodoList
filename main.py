from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from database import engine
from database import Base

from routing.cadastro import cadastro_router
from routing.tarefa import tarefa_router
from routing.token import token_router

from sqlalchemy.orm import Session

from database import get_db

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def home():
    return "API de Trabalho da Faculdade."

app.mount("/static", StaticFiles(directory="frontend"), name="static")

app.include_router(cadastro_router, prefix="/cadastro", tags=["cadastro"])
app.include_router(tarefa_router, prefix="/tarefa", tags=["tarefa"])
app.include_router(token_router, prefix="/token", tags=["token"])
