from pydantic import BaseModel

class TarefaCadastroCreate(BaseModel):
    tarefa_id: int

class TarefaCadastro(TarefaCadastroCreate):
    cadastro_id: int
    id: int