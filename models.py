from sqlalchemy import Column, String, Integer, Time, Date, Boolean, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship, sessionmaker
from database import Base


class Cadastro(Base):

    __tablename__ = 'cadastro'
    id = Column(Integer, primary_key=True)
    username = Column(String(length=24), nullable=False, unique=True)
    password_hash = Column(String(length=60), nullable=False)
    
    tarefa = relationship("Tarefa", backref=__tablename__)

class Tarefa(Base):

    __tablename__ = 'tarefa'
    id = Column(Integer, primary_key=True)
    descricao = Column(String(length=512), nullable=False)
    data_inicio = Column(Date(), nullable=False)
    data_fim = Column(Date(), nullable=False)
    ativo = Column(Boolean(), default=False)
    responsavel_id = Column(Integer(), ForeignKey("cadastro.id"), nullable=False)

class TarefaCadastroAssociation(Base):

    __tablename__ = 'tarefa_cadastro'
    id = Column(Integer, primary_key=True)
    tarefa_id = Column(Integer(), ForeignKey("tarefa.id"), nullable=False)
    cadastro_id = Column(Integer(), ForeignKey("cadastro.id"), nullable=False)