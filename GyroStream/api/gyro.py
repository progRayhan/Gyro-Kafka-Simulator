from fastapi import APIRouter
from _applibs.gyroscope_simulator import GyroscopeSimulator

router = APIRouter()
gyro = GyroscopeSimulator()

@router.get("/gyro-data")
async def get_gyro_data():
    data = gyro.generate_data()
    return data
