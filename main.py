from fastapi import FastAPI,Depends
from functools import lru_cache
from typing import Annotated
from .config import Settings


@lru_cache
def get_setting():
    return Settings()


app = FastAPI()

@app.get('/info',response_model=Settings)
def get_info(settings : Annotated[Settings,Depends(get_setting)]):
    return settings

