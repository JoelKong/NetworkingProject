import paho.mqtt.client as mqtt
import json
from gpiozero import AngularServo
import threading
import time

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

# Global variable to control the motor thread
motor_active = False
motor_thread = None

# Callback when the client receives a CONNACK response from the server
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(CONTROL_TOPIC)

# Callback when a PUBLISH message is received from the server
def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    if data.get("action") == "activate":
        start_motor()
    elif data.get("action") == "deactivate":
        stop_motor()

# Function to run the motor (servo) in a separate thread
def motor_control():
    global motor_active
    while motor_active:
        for angle in range(-90, 91, 5):  # Increment from -90 to 90 degrees in steps of 5
            if not motor_active:
                break
            servo.angle = angle
            time.sleep(0.1)
        time.sleep(2)  # Pause for 2 seconds when reaching 90 degrees
        for angle in range(90, -91, -5):  # Decrement from 90 to -90 degrees in steps of 5
            if not motor_active:
                break
            servo.angle = angle
            time.sleep(0.1)
        print("Motor activated")
    servo.angle = 0  # Set servo back to original position when deactivated
    print("Motor deactivated")

# Function to start the motor thread
def start_motor():
    global motor_active, motor_thread
    if not motor_active:
        motor_active = True
        motor_thread = threading.Thread(target=motor_control)
        motor_thread.start()

# Function to stop the motor thread
def stop_motor():
    global motor_active, motor_thread
    motor_active = False
    if motor_thread is not None:
        motor_thread.join()

# Set MQTT client callbacks
client.on_connect = on_connect
client.on_message = on_message

# Connect to MQTT broker
client.connect(BROKER, PORT, 60)

# Start the MQTT client loop to process received messages
client.loop_forever()
