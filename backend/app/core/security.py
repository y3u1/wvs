from fastapi import HTTPException,status
from typing import Annotated
from pydantic import AfterValidator,Field
from fastapi.security import OAuth2PasswordBearer
import pwdlib
import re

def check_password_complicated(psd : str):
    errors = []
        
    if not re.search(r'[A-Z]', v):
        errors.append("至少包含一个大写字母")
    if not re.search(r'[a-z]', v):
        errors.append("至少包含一个小写字母")
    if not re.search(r'\d', v):
        errors.append("至少包含一个数字")
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', v):
        errors.append("至少包含一个特殊字符")
    
    if errors :
        raise ValueError(errors)
    else :
        return

GoodPwd = Annotated[str,Field(ge=8),AfterValidator(check_password_complicated)]
