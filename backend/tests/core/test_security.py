import sys
sys.path.append("..")
from app.core.security import (
    GoodPwd,
    hash_password,
    verify_password
)
from pydantic import ValidationError,BaseModel
from pwdlib.exceptions import UnknownHashError
import pytest

# test Goodpwd
class pwdmodel(BaseModel):
    pwd : GoodPwd

class TestGoodPwd:
    def test_len_7(self):
        with pytest.raises(ValidationError) :
            pwdmodel(pwd='Aa1235@')
    def test_char_with_no_upper(self):
        with pytest.raises(ValidationError) :
            pwdmodel(pwd='aa123456@')
    def test_char_with_no_lower(self):
        with pytest.raises(ValidationError) :
            pwdmodel(pwd='AA123456@')
    def test_char_with_no_number(self):
        with pytest.raises(ValidationError) :
            pwdmodel(pwd='AAAAAaaaaa@')
    def test_char_with_no_special_char(self):
        with pytest.raises(ValidationError) :
            pwdmodel(pwd='Aa1234567')

class TestHashPwd:
    plain_pwd : str = 'Plain_Pwd123@'
    hash_password : str = ''
    def test_hash_pwd(self):
        try:
            assert pwdmodel(pwd=self.plain_pwd).pwd == self.plain_pwd
        except ValidationError as e:
            pytest.fail(f"password is not good: {e}")
        
        hashed_pwd : str = hash_password(self.plain_pwd)
        try:
            res = verify_password(plain_password=self.plain_pwd,hashed_password=hashed_pwd)
            assert res == True
        except UnknownHashError as e:
            pytest.fail(f"password hash failed: {e}")


        
