from sqlmodel import (
    SQLModel,
    Field,
    Relationship,
)
from pydantic import HttpUrl
from datetime import datetime
from enum import Enum

# 用户表
class UserBase(SQLModel):
    name : str

class User(UserBase,table = True):
    id : int | None = Field(primary_key=True,default=None)
    password_hash : str
    is_admin : bool

class UserCreate(UserBase):
    password : str

class UserPublic(UserBase):
    id: int


# 漏洞信息表
# 可同时指定多种漏洞扫描

class VulnType(Enum):
    XSS = 0
    CSRF = 1
    FILE_UPLOAD = 2
    FILE_INCLUDE = 4
    FILE_DOWNLOAD = 8
    URL_REDIRECT = 16
class Status(Enum):
    WAITTING = 0
    RUNNING = 1
    FINISHED = 2

# 漏洞信息
class Vulnerabilitiy(SQLModel,table=True):
    id : int | None  = Field(primary_key=True,default=None)
    cve_id : str | None
    description : str | None
    fix_suggestion : str | None

# 任务
class TaskBase(SQLModel):
    submit_time : datetime 
    finished_time : datetime | None = None
    status : Status 
# 扫描任务
class ScanTask(TaskBase,table=True): 
    id : int | None = Field(primary_key=True,default=None) 
    scan_type : VulnType 
    url : HttpUrl  
    celery_taskid : str = Field(foreign_key='celerytask.taskid')
    user_id : int = Field(foreign_key='user.id')
#celery 任务
class CeleryTask(TaskBase,table=True):
    taskid : str = Field(primary_key=True)

