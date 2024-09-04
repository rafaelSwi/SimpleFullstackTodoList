from typing import List
from pydantic import BaseModel
from datetime import date

class TarefaCreate(BaseModel):
    descricao: str
    data_inicio: date
    data_fim: date

class Tarefa(TarefaCreate):
    responsavel_id: int
    ativo: bool
    id: int