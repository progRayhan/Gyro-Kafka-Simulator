from fastapi import FastAPI
from gyroscope_simulator import GyroscopeSimulator

app = FastAPI()

gyro = GyroscopeSimulator()

@app.get("/gyro-data/")
async def get_gyro_data():
    data = gyro.generate_data()
    return data
