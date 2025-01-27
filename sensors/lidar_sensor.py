import numpy as np
from sensors.base_sensor import BaseSensor

class LidarSensor(BaseSensor):
    def read_data(self):
        """Simulate LiDAR point cloud (x, y, z)."""
        num_points = 100
        return np.random.rand(num_points, 3) * 10  # 100 points in 3D space

    def process_data(self, data):
        """Example: Count points above a certain threshold."""
        return len(data[data[:, 2] > 5])  # Points with z > 5
