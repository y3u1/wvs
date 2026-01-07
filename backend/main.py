from fastapi import FastAPI,Depends
from functools import lru_cache
from .config import Settings
from typing import Annotated


app = FastAPI()

@lru_cache
def get_settings():
    return Settings()




@app.get('/info',response_model=Settings)
async def get_info(settings : Annotated[Settings,Depends(get_settings)]):
    return settings


    