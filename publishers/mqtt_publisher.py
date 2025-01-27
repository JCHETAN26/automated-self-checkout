import paho.mqtt.client as mqtt

class MQTTPublisher:
    def __init__(self, broker='test.mosquitto.org', port=1883):
        self.client = mqtt.Client()
        self.client.connect(broker, port, 60)

    def publish(self, topic, message):
        self.client.publish(topic, message)
