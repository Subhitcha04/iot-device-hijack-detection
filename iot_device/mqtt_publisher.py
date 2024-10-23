import paho.mqtt.client as mqtt
import random
import time
import json

MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 1883
MQTT_TOPIC = "iot/sensor"

def generate_sensor_data():
    # Simulate temperature and humidity sensor data
    temperature = round(random.uniform(20.0, 35.0), 2)
    humidity = round(random.uniform(30.0, 70.0), 2)
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    return {
        'temperature': temperature,
        'humidity': humidity,
        'timestamp': timestamp
    }

# Initialize MQTT client
client = mqtt.Client()
client.connect(MQTT_BROKER, MQTT_PORT, 60)

while True:
    # Generate and publish sensor data
    sensor_data = generate_sensor_data()
    client.publish(MQTT_TOPIC, json.dumps(sensor_data))
    print(f"Published data: {sensor_data}")
    time.sleep(5)  # Send data every 5 seconds
