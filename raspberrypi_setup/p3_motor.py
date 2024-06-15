import paho.mqtt.client as mqtt
import json

# MQTT Broker details
BROKER = "garden"
PORT = 1883
CONTROL_TOPIC = "control/motor"

# Callback when the client receives a CONNACK response from the server
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(CONTROL_TOPIC)

# Callback when a PUBLISH message is received from the server
def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    if data.get("action") == "activate":
        activate_motor()

def activate_motor():
    # Code to activate the motor
    print("Motor activated")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)

# Start the loop to process received messages
client.loop_forever()
