from database import get_db
from encryption.functions import get_current_user
from fastapi import Depends
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from typing import Annotated

DB_DEPENDENCY = Annotated[Session, Depends(get_db)]
USER_DEPENDENCY = Annotated[dict, Depends(get_current_user)]