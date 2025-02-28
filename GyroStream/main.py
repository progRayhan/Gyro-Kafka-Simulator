from fastapi import FastAPI
from api import gyro

app = FastAPI()

app.include_router(gyro.router)
