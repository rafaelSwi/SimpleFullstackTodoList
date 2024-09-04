import platform
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_URL = ''
if platform.system() == "Linux":
    DB_URL = 'postgresql://postgres:postgres@localhost/trabalho'
elif platform.system() == "Darwin":
    DB_URL = 'postgresql://postgres:admin@localhost/first_test'
else:
    print("os nao programado.")
    exit()

engine = create_engine(DB_URL)

SessionLocal = sessionmaker(autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()