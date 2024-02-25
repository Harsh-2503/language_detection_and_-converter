from typing import Union
from fastapi import FastAPI
from src.routers import v1_router


app = FastAPI()
app.include_router(v1_router.router, prefix='/v1')

