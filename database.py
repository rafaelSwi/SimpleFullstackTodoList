import platform
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import json

def confidencial():
    with open("database.json", 'r') as file:
        data = json.load(file)
    return data

DATABASE_NAME = confidencial().get('database_name')
POSTGRESL_PSW = confidencial().get('postgresql_password')

<<<<<<< HEAD
DB_URL = 'postgresql://postgres@localhost/gabriel_diniz'
=======
DB_URL = f'postgresql://postgres:{POSTGRESL_PSW}@localhost/{DATABASE_NAME}'
>>>>>>> origin/master

engine = create_engine(DB_URL)

SessionLocal = sessionmaker(autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()