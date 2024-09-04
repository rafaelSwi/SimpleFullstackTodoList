from typing import List
from pydantic import BaseModel
from datetime import date

class TarefaCreate(BaseModel):
    descricao: str
    data_inicio: date
    data_fim: date
    ativo: bool

class Tarefa(TarefaCreate):
    responsavel_id: int
    id: int