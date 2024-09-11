from fastapi import FastAPI, Depends
from database import engine
from database import Base
from routing.cadastro import cadastro_router
from routing.tarefa import tarefa_router
from routing.token import token_router
from sqlalchemy.orm import Session
from database import get_db
from fastapi.middleware.cors import CORSMiddleware  # Import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Add CORS middleware here
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, you can restrict this to specific domains
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def home():
    return "API de Trabalho da Faculdade."

# Include your routers
app.include_router(cadastro_router, prefix="/cadastro", tags=["cadastro"])
app.include_router(tarefa_router, prefix="/tarefa", tags=["tarefa"])
app.include_router(token_router, prefix="/token", tags=["token"])
