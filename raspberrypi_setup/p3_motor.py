import paho.mqtt.client as mqtt
import json
from gpiozero import AngularServo
import RPi.GPIO as GPIO

# MQTT Broker details
BROKER = "192.168.1.10"
PORT = 1883
CONTROL_TOPIC = "control/motor"

# Servo motor setup
PIN_SERVO = 18  # Example GPIO pin for servo motor

# Initialize servo motor
servo = AngularServo(PIN_SERVO, min_angle=-90, max_angle=90)  # Adjust min and max angles as per your servo specifications

# MQTT client setup
client = mqtt.Client()

# Callback when the client receives a CONNACK response from the server
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(CONTROL_TOPIC)

# Callback when a PUBLISH message is received from the server
def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    if data.get("action") == "activate":
        activate_motor()
    elif data.get("action") == "deactivate":
        deactivate_motor()

# Function to activate the motor (servo)
def activate_motor():
    servo.angle = 90  # Set servo to maximum angle (clockwise)
    print("Motor activated")

# Function to deactivate the motor (servo)
def deactivate_motor():
    servo.angle = 0  # Set servo back to original position (or any desired position for deactivation)
    print("Motor deactivated")

# Ultrasonic Scanner to detect Object (Stepper Motor to facilitate scanning)


# Set MQTT client callbacks
client.on_connect = on_connect
client.on_message = on_message

# Connect to MQTT broker
client.connect(BROKER, PORT, 60)

# Start the MQTT client loop to process received messages
client.loop_forever()

