from pydantic_settings import BaseSettings,SettingsConfigDict
from pydantic import BaseModel


class Settings(BaseSettings):
    db_passwd : str
    db_user : str
    model_config = SettingsConfigDict(env_file="../.env")

