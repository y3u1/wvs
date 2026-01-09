from sqlmodel import (
    SQLModel,
    Field,
    Relationship,
)
from pydantic import HttpUrl
from datetime import datetime
from enum import Enum
from core.security import GoodPwd
# 用户表
class UserBase(SQLModel):
    name : str = Field(unique=True,index=True)

class User(UserBase,table = True):
    id : int | None = Field(primary_key=True,default=None,index=True)
    password_hash : str
    tasks : list["ScanTask"] | None = Relationship(back_populates="own_user")
    create_at : datetime = Field(default_factory=datetime.now)
    is_admin : bool = False


class UserCreate(UserBase):
    password : GoodPwd

class UserPublic(UserBase):
    id: int

class UerUpdate(UserBase):
    new_password : GoodPwd
    current_password : GoodPwd


# 漏洞信息表
# 可同时指定多种漏洞扫描

class VulnType(Enum):
    XSS = 0
    CSRF = 1
    FILE_UPLOAD = 2
    FILE_INCLUDE = 4
    FILE_DOWNLOAD = 8
    URL_REDIRECT = 16
    @classmethod
    def has_type(cls, value: int, vuln_type: 'VulnType') -> bool:
        return bool(value & vuln_type.value)
    
class Status(Enum):
    WAITTING = "waiting"
    RUNNING = "running"
    FINISHED = "finished"
    FAILED = "failed"

# 漏洞信息
class Vulnerability(SQLModel,table=True):
    id : int | None  = Field(primary_key=True,default=None)
    cve_id : str | None = Field(index=True)
    description : str | None
    fix_suggestion : str | None

# 任务
class TaskBase(SQLModel):
    submit_time : datetime
    finished_time : datetime | None = None
    status : Status 
# 扫描任务 要求所有扫描任务都由于celery调度执行
class ScanTask(TaskBase,table=True): 
    id : int | None = Field(primary_key=True,default=None) 
    scan_type : int # 可能同时是多种扫描类型
    url : HttpUrl  
    celery_taskid : str = Field(foreign_key='celerytask.taskid')
    user_id : int = Field(foreign_key='user.id')
    own_user : User = Relationship(back_populates="tasks")

#celery 任务
class CeleryTask(TaskBase,table=True):
    taskid : str = Field(primary_key=True)

