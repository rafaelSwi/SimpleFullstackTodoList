from encryption.functions import authenticate_user, get_password_hash
from schemas.tarefa import TarefaCreate
import models as model

def get_all_tarefas(db: authenticate_user, skip:int=0, limit:int=150):
    return db.query(model.Tarefa).offset(skip).limit(limit).all()

def get_tarefa_by_id(db: authenticate_user, tarefa_id: int):
    return db.query(model.Tarefa).filter(model.Tarefa.id == tarefa_id).first()

def get_tarefas_associated_with_logged_user(db: authenticate_user, user):
    cadastro_id = user.get('id')
    tarefa_cadastro_list = db.query(model.TarefaCadastroAssociation).filter(model.TarefaCadastroAssociation.cadastro_id == cadastro_id).all()
    tarefas_list = []
    for i in tarefa_cadastro_list:
        tarefas_list.append(get_tarefa_by_id(db=db, tarefa_id=i.tarefa_id))
    return tarefas_list

def create_tarefa(db: authenticate_user, user, tarefa: TarefaCreate):
    _tarefa = model.Tarefa(
        descricao = tarefa.descricao,
        data_inicio = tarefa.data_inicio,
        data_fim = tarefa.data_fim,
        ativo = True,
        responsavel_id = user.get('id')
    )
    db.add(_tarefa)
    db.commit()
    db.refresh(_tarefa)
    return _tarefa