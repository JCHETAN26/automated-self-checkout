from influxdb import InfluxDBClient

class GrafanaPublisher:
    def __init__(self, host="localhost", port=8086, database="sensors"):
        self.client = InfluxDBClient(host=host, port=port)
        self.client.switch_database(database)

    def publish(self, measurement, value):
        data = [{
            "measurement": measurement,
            "fields": {"value": value}
        }]
        self.client.write_points(data)
