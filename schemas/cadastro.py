from typing import List
from pydantic import BaseModel

class CadastroCreate(BaseModel):
    username: str
    password: str

class Cadastro(CadastroCreate):
    id: int
    tarefa: List[int] = [] 