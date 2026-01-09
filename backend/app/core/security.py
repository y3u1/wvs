from typing import Annotated
from pydantic import AfterValidator,Field
from fastapi.security import OAuth2PasswordBearer
from pwdlib import PasswordHash
import re

def check_password_complicated(pwd : str):
    errors = []
        
    if not re.search(r'[A-Z]', pwd):
        errors.append("至少包含一个大写字母")
    if not re.search(r'[a-z]', pwd):
        errors.append("至少包含一个小写字母")
    if not re.search(r'\d', pwd):
        errors.append("至少包含一个数字")
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', pwd):
        errors.append("至少包含一个特殊字符")
    
    if errors :
        raise ValueError(errors)
    else :
        return pwd

GoodPwd = Annotated[str,Field(min_length=8),AfterValidator(check_password_complicated)]

# fastapi security

# password hash
pwd_hash = PasswordHash.recommended()

def hash_password(plain_password : str) -> str:
    return pwd_hash.hash(plain_password)

def verify_password(*,hashed_password : str,plain_password : str) -> bool:
    return pwd_hash.verify(plain_password, hashed_password)




