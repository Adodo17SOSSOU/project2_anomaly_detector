import random
import time

class DataGenerator:
    def __init__(self, max_value=200, anomaly_chance=0.05):
        self.max_value = max_value
        self.anomaly_chance = anomaly_chance

    def generate(self):
        """Generate one set of sensor readings."""
        data = {
            'sensor1': random.uniform(0, self.max_value),
            'sensor2': random.uniform(0, self.max_value),
            'sensor3': random.uniform(0, self.max_value),
        }

        # Occasionally introduce an anomaly
        if random.random() < self.anomaly_chance:
            sensor_to_spike = random.choice(list(data.keys()))
            data[sensor_to_spike] *= random.uniform(2, 5)

        return data

