from sqlmodel import Session
from models import UserCreate,User,UserPublic
from core.security import hash_password


# User
def create_user(*,session : Session,usercreate : UserCreate):
    us : User = User.model_validate(
        usercreate,
        update = {'password_hash' : hash_password(usercreate.password)},
    )
    session.add(us)
    session.commit()
    session.refresh(us)
    return us



def get_user_by_name(*,session : Session,userpublic : UserPublic):

    pass
def get_user_by_id(*,session : Session,):
    pass

def update_user_password():
    pass

def delete_user():
    pass

def get_user_tasks():
    pass

