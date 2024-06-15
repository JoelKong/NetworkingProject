import paho.mqtt.client as mqtt
import time
import json
import requests

# MQTT Broker details
BROKER = "garden"
PORT = 1883
DATA_TOPIC = "data/gardendata"

# Flask server URL
FLASK_SERVER_URL = "http://<FLASK_SERVER_IP>:5000/update"

# Variables to store sensor data
sensor_data = {
    "temperature": 0,
    "humidity": 0
}

# Callback when the client receives a CONNACK response from the server
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(DATA_TOPIC)

# Callback when a PUBLISH message is received from the server
def on_message(client, userdata, msg):
    global sensor_data
    data = json.loads(msg.payload.decode())
    sensor_data["temperature"] = data.get("temperature", 0)
    sensor_data["humidity"] = data.get("humidity", 0)
    print(f"Received message: {sensor_data}")


# Send data to Flask server
def send_data_to_frontend():
    try:
        response = requests.post(FLASK_SERVER_URL, json=sensor_data)
        print(f"Data sent to frontend: {sensor_data}, Response: {response.status_code}")
    except Exception as e:
        print(f"Failed to send data to frontend: {e}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)

# Start the loop to process received messages
client.loop_start()

try:
    while True:
        send_data_to_frontend()
        time.sleep(10)
except KeyboardInterrupt:
    print("Exiting...")
    client.loop_stop()
    client.disconnect()
