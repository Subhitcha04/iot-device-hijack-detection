import paho.mqtt.client as mqtt
import json
import tensorflow as tf  # Import TensorFlow
from pymongo import MongoClient
import os

# MongoDB setup
client = MongoClient('mongodb://localhost:27017/')
db = client['iot_database']
collection = db['sensor_data']

# Define the path to the pretrained SVM model
model_path = r'C:\cit\IoT23-Malware-Detection\Notebooks\finalizedSVM_model.sav'  # SVM model path

# Load the pretrained SVM model using TensorFlow
try:
    svm_model = tf.keras.models.load_model(model_path)
except Exception as e:
    print(f"Error loading model: {e}")

# Preprocess data for SVM prediction
def preprocess_data(data):
    # Extract features like temperature and humidity from incoming data
    features = [[data['temperature'], data['humidity']]]
    return features

# Detect anomaly using the pretrained SVM model
def detect_anomaly(data):
    features = preprocess_data(data)
    prediction = svm_model.predict(features)
    return prediction[0] == 1  # Assuming '1' indicates anomaly

# Callback function for when an MQTT message is received
def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    print(f"Received data: {data}")

    # Detect anomalies using the pretrained SVM model
    is_anomaly = detect_anomaly(data)
    data['anomaly'] = is_anomaly

    # Store the result in MongoDB
    collection.insert_one(data)
    print(f"Data stored in MongoDB: {data}")

# MQTT connection settings
MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 1883
MQTT_TOPIC = "iot/sensor"

# MQTT connect callback
def on_connect(client, userdata, flags, rc):
    print(f"Connected to MQTT broker with result code {rc}")
    client.subscribe(MQTT_TOPIC)

# Set up the MQTT client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker and start listening for messages
client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.loop_forever()
