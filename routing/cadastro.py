from encryption.constants import USER_DEPENDENCY
from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session
from crud.cadastro import create_cadastro, get_all_cadastros
from database import get_db
from schemas.cadastro import CadastroCreate

cadastro_router = APIRouter()


# COLETA TODOS OS USUARIOS CRIADOS
@cadastro_router.get('/all')
async def _get_all(user: USER_DEPENDENCY, db: Session = Depends(get_db)):
    return get_all_cadastros(db=db)


# CRIA UM NOVO USUARIO
@cadastro_router.post('/create')
async def _create(request: CadastroCreate, db: Session = Depends(get_db)):
    return create_cadastro(db, cadastro=request)