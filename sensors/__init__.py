from abc import ABC, abstractmethod

class BaseSensor(ABC):
    @abstractmethod
    def read_data(self):
        """Simulate or read data from the sensor."""
        pass

    @abstractmethod
    def process_data(self):
        """Process raw sensor data."""
        pass
