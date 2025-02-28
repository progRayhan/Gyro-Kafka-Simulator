import time
import random


class GyroscopeSimulator:
    def __init__(self, min_value=-500, max_value=500, interval=1):
        self.min_value = min_value
        self.max_value = max_value
        self.interval = interval

    def generate_data(self):
        data = {
            "timestamp": time.time(),
            "x": round(random.uniform(self.min_value, self.max_value)),
            "Y": round(random.uniform(self.min_value, self.max_value)),
            "z": random.uniform(self.min_value, self.max_value),
        }
        return data
