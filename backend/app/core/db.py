from sqlmodel import create_engine,SQLModel,Session,delete
from .config import settings

engine = create_engine(str(settings.DATABASE_URI))



def init_db():
    pass