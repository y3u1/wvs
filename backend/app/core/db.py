from sqlmodel import create_engine,SQLModel,Session,delete
from .config import settings

engine = create_engine(str(settings.DATABASE_URI))


def get_session():
    with Session(engine) as session:
        yield session

def init_db():
    
    pass