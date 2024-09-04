from encryption.functions import authenticate_user
from crud.tarefa import get_tarefa_by_id
from crud.cadastro import get_cadastro_by_id
from schemas.tarefa_cadastro import TarefaCadastroCreate
import models as model


def get_tarefas_associated_with_logged_user(db: authenticate_user, user, only_active_tasks: bool = False):
    cadastro_id = user.get('id')
    tarefa_cadastro_list = db.query(model.TarefaCadastroAssociation).filter(model.TarefaCadastroAssociation.cadastro_id == cadastro_id).all()
    tarefas_list = []
    for i in tarefa_cadastro_list:
        _tarefa = get_tarefa_by_id(db=db, tarefa_id=i.tarefa_id)
        if only_active_tasks:
            if _tarefa.ativo == True:
                tarefas_list.append(_tarefa)
        else:
            tarefas_list.append(_tarefa)
    return tarefas_list

def create_tarefa_cadastro_association(db: authenticate_user, user, association: TarefaCadastroCreate):
    if not get_cadastro_by_id(db=db, cadastro_id=user.get('id')):
        print("We tried to create a tarefa_cadastro association, but the cadastro ID doesn't exist.")
        return None
    _tarefa_cadastro = model.TarefaCadastroAssociation(
        tarefa_id=association.tarefa_id,
        cadastro_id=user.get('id')
    )
    db.add(_tarefa_cadastro)
    db.commit()
    db.refresh(_tarefa_cadastro)
    return _tarefa_cadastro
