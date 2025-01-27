import random
from sensors.base_sensor import BaseSensor

class WeightSensor(BaseSensor):
    def read_data(self):
        """Simulate weight data."""
        return random.uniform(0, 100)  # Random weight between 0 and 100 kg

    def process_data(self, data):
        """Simple processing (e.g., round to 2 decimal places)."""
        return round(data, 2)
