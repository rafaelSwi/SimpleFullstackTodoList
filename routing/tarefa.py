from encryption.constants import USER_DEPENDENCY
from fastapi import APIRouter, Depends, Response
from crud.tarefa import create_tarefa, get_tarefa_by_id
from crud.tarefa_cadastro import create_tarefa_cadastro_association
from database import get_db
from schemas.tarefa_cadastro import TarefaCadastroCreate
from sqlalchemy.orm import Session
from schemas.tarefa import TarefaCreate
from schemas.tarefa_cadastro import TarefaCadastroCreate, TarefaCadastro
from crud.tarefa_cadastro import get_tarefas_associated_with_logged_user

tarefa_router = APIRouter()


# RETORNA UMA TAREFA ESPECIFICA
@tarefa_router.get('/{tarefa_id}')
async def _get_tarefas_associated_with_logged_user(user: USER_DEPENDENCY, tarefa_id: int, db: Session = Depends(get_db)):
    _tarefa = get_tarefa_by_id(db=db, tarefa_id=tarefa_id)
    if _tarefa:
        return _tarefa
    else:
        return Response(status_code=404)

# DEFINE UMA TAREFA COMO ATIVO=FALSO PARA FIRMAR QUE FOI CONCLUIDA
@tarefa_router.put('/{tarefa_id}/check')
async def _get_tarefas_associated_with_logged_user(user: USER_DEPENDENCY, tarefa_id: int, db: Session = Depends(get_db)):
    _tarefa = get_tarefa_by_id(db=db, tarefa_id=tarefa_id)
    if _tarefa:
        if not _tarefa.ativo:
            return Response(status_code=417)
        _tarefa.ativo = False
        db.commit()
        db.refresh(_tarefa)
        return Response(status_code=200)
    else:
        return Response(status_code=404)

# RETORNA UMA LISTA DE TAREFAS CRIADAS PELO USUARIO LOGADO
@tarefa_router.get('/list')
async def _get_tarefas_associated_with_logged_user(user: USER_DEPENDENCY, db: Session = Depends(get_db)):
    try:
        return get_tarefas_associated_with_logged_user(db=db, user=user)
    except:
        return Response(status_code=500)


# RETORNA UMA LISTA DE TAREFAS CRIADAS PELO USUARIO LOGADO DEFINIDAS COMO ATIVAS
@tarefa_router.get('/worklist')
async def _get_tarefas_associated_with_logged_user(user: USER_DEPENDENCY, db: Session = Depends(get_db)):
    try:
        return get_tarefas_associated_with_logged_user(db=db, user=user, only_active_tasks=True)
    except:
        return Response(status_code=500)


# CRIA UMA NOVA TAREFA E SUAS ASSOCIACOES
@tarefa_router.post('/create')
async def _create(user: USER_DEPENDENCY, request: TarefaCreate, db: Session = Depends(get_db)):
    _tarefa = create_tarefa(db=db, user=user, tarefa=request)
    _tarefa_cadastro_create = TarefaCadastroCreate(tarefa_id=_tarefa.id)
    create_tarefa_cadastro_association(db=db, user=user, association=_tarefa_cadastro_create)
    return Response(status_code=200)
