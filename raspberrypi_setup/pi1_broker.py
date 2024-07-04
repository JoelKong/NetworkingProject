import paho.mqtt.client as mqtt
import time
import json
from flask import Flask, request, jsonify
import threading

# MQTT Broker details
BROKER = "192.168.1.10"
PORT = 1883
DATA_TOPIC = "data/gardendata"

# Default sensor data
sensor_data = {
    "temperature": 0,
    "humidity": 0,
    "distance1": 0,
    "distance2": 0,
    "image": None,
}

# Subscribe to data topic
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(DATA_TOPIC)

# Getting data from the topic (decoding)
def on_message(client, userdata, msg):
    global sensor_data
    data = json.loads(msg.payload.decode())
    sensor_data["temperature"] = data.get("temperature", 0)
    sensor_data["humidity"] = data.get("humidity", 0)
    sensor_data["distance1"] = data.get("distance1", 0)
    sensor_data["distance2"] = data.get("distance2", 0)
    sensor_data["image"] = data.get("image", None)
    print(f"Received message: {sensor_data}")

# Run MQTT on loop
def run_mqtt_client():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(BROKER, PORT, 60)

    # Start the loop to process received messages
    client.loop_start()

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        print("Exiting...")
        client.loop_stop()
        client.disconnect()

# Flask server setup
app = Flask(__name__)

@app.route('/data', methods=['POST'])
def receive_data():
    global sensor_data
    sensor_data = request.json
    print(f"Data received via POST: {sensor_data}")
    return jsonify({"status": "success"}), 200

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(sensor_data), 200

def run_flask_server():
    app.run(host='0.0.0.0', port=5000)

# Run both MQTT client and Flask server in separate threads
mqtt_thread = threading.Thread(target=run_mqtt_client)
flask_thread = threading.Thread(target=run_flask_server)

mqtt_thread.start()
flask_thread.start()

mqtt_thread.join()
flask_thread.join()
