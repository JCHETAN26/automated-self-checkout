import yaml
from sensors.weight_sensor import WeightSensor
from sensors.lidar_sensor import LidarSensor
from publishers.mqtt_publisher import MQTTPublisher
from publishers.kafka_publisher import KafkaPublisher
from publishers.grafana_publisher import GrafanaPublisher

# Load configuration
with open("config/config.yaml", "r") as file:
    config = yaml.safe_load(file)

# Initialize sensors and publishers
sensors = []
if config["sensors"]["weight"]:
    sensors.append(WeightSensor())
if config["sensors"]["lidar"]:
    sensors.append(LidarSensor())

publishers = []
if config["publish_to"]["mqtt"]:
    publishers.append(MQTTPublisher())
if config["publish_to"]["kafka"]:
    publishers.append(KafkaPublisher())
if config["publish_to"]["grafana"]:
    publishers.append(GrafanaPublisher())

# Read, process, and publish sensor data
for sensor in sensors:
    data = sensor.read_data()
    processed = sensor.process_data(data)
    for publisher in publishers:
        publisher.publish(f"{sensor.__class__.__name__}_data", str(processed))
