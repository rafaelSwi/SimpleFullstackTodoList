from fastapi import HTTPException
from encryption.functions import authenticate_user, get_password_hash
from schemas.cadastro import CadastroCreate
import models as model

def get_all_cadastros(db: authenticate_user, skip:int=0, limit:int=150):
    return db.query(model.Cadastro).offset(skip).limit(limit).all()

def get_cadastro_by_id(db: authenticate_user, cadastro_id: int):
    return db.query(model.Cadastro).filter(model.Cadastro.id == cadastro_id).first()

def create_cadastro(db: authenticate_user, cadastro: CadastroCreate):
    # Check if username already exists
    existing_user = db.query(model.Cadastro).filter(model.Cadastro.username == cadastro.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already taken")

    # If username does not exist, proceed with creating the user
    _cadastro = model.Cadastro(
        username=cadastro.username,
        password_hash=get_password_hash(cadastro.password),
    )
    
    db.add(_cadastro)
    db.commit()
    db.refresh(_cadastro)
    return _cadastro
