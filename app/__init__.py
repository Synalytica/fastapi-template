from fastapi import FastAPI

from .core import core


app = FastAPI()

# include various APIs
app.include_router(core, prefix="/core")
