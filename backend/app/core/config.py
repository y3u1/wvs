from pydantic_settings import BaseSettings,SettingsConfigDict
from pydantic import (
    PostgresDsn,
    AnyUrl,
    
    computed_field,
    RedisDsn,

)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='../.env',
        env_ignore_empty=True,
        extra="ignore",
        )
    
    API_V1_STR : str = '/api/v1'

    SUPERUSER : str
    SUPERUSER_PASSWORD : str
    
    SECRET_KEY : str
    ALGORITHM : str
    ACCESS_TOKEN_EXPIRE_MINUTES : int
    #front web configuration


    # postgres configuration
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_PASSWORD: str | None = None
    POSTGRES_USER: str
    POSTGRES_DB: str 

    @computed_field
    @property
    def WVS_DATABASE_URI(self) -> PostgresDsn:
        return PostgresDsn.build(
            scheme="postgresql",
            username=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_HOST,
            port=self.POSTGRES_PORT,
            path=self.POSTGRES_DB,
        )
    
    #celery configuration
    #celery Redis 
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_PASSWORD: str | None = None
    REDIS_DB: int = 0  # 默认使用 0 号数据库
    REDIS_SSL: bool = False  # 是否使用 SSL

    @computed_field
    @property
    def CELERY_BROKER_URI(self) -> RedisDsn:
        return RedisDsn.build(
            scheme="redis",
            password=self.REDIS_PASSWORD,
            host=self.REDIS_HOST,
            port=self.REDIS_PORT,
            path=self.REDIS_DB,
        )
    
    #celery result backend

    RESULT_BACKEND_POSTGRES_HOST : str = 'localhost'
    RESULT_BACKEND_POSTGRES_PORT : int = 5432
    RESULT_BACKEND_POSTGRES_USER : str 
    RESULT_BACKEND_POSTGRES_PASSWORD : str | None = None
    RESULT_BACKEND_POSTGRES_DB : str
    @computed_field
    @property
    def CELERY_RESULT_BACKEND_URI(self) -> PostgresDsn:
        return PostgresDsn.build(
            scheme="postgresql",
            username=self.RESULT_BACKEND_POSTGRES_USER,
            password=self.RESULT_BACKEND_POSTGRES_PASSWORD,
            host=self.RESULT_BACKEND_POSTGRES_HOST,
            port=self.RESULT_BACKEND_POSTGRES_PORT,
            path=self.RESULT_BACKEND_POSTGRES_DB,
        )
   

    

settings = Settings()