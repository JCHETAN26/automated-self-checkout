from kafka import KafkaProducer

class KafkaPublisher:
    def __init__(self, broker='localhost:9092'):
        self.producer = KafkaProducer(bootstrap_servers=broker)

    def publish(self, topic, message):
        self.producer.send(topic, value=message.encode('utf-8'))
        self.producer.flush()
