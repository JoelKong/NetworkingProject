import paho.mqtt.client as mqtt
import Adafruit_DHT
import json
import time

# MQTT Broker details
BROKER = "garden"
PORT = 1883
DATATOPIC = "data/gardendata"
CONTROL_TOPIC = "control/motor"

# DHT22 Sensor setup
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

client = mqtt.Client()

# Callback when the client receives a CONNACK response from the server
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

client.on_connect = on_connect

client.connect(BROKER, PORT, 60)

client.loop_start()

try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        if humidity is not None and temperature is not None:
            sensor_data = {
                "temperature": temperature,
                "humidity": humidity
            }
            client.publish(DATATOPIC, json.dumps(sensor_data))
            print(f"Published data: {sensor_data}")

            # Check temperature and send control message to Pi3 if needed
            if temperature > 35:
                client.publish(CONTROL_TOPIC, json.dumps({"action": "activate"}))
                print("Motor activation message sent")
                # send whatsapp message through twillo api

        time.sleep(10)
except KeyboardInterrupt:
    print("Exiting...")
    client.loop_stop()
    client.disconnect()
