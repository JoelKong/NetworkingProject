import time
import json
import adafruit_dht
import board
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt

# MQTT Broker details
BROKER = "192.168.1.10"
PORT = 1883

# MQTT Topics
DATATOPIC = "data/gardendata"
CONTROL_TOPIC = "control/motor"

# DHT22 Sensor setup
DHT_SENSOR = adafruit_dht.DHT22(board.D4)

# GPIO setup for first ultrasonic sensor
PIN_TRIGGER1 = 7
PIN_ECHO1 = 11

# GPIO setup for second ultrasonic sensor
PIN_TRIGGER2 = 13
PIN_ECHO2 = 15

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN_TRIGGER1, GPIO.OUT)
GPIO.setup(PIN_ECHO1, GPIO.IN)
GPIO.setup(PIN_TRIGGER2, GPIO.OUT)
GPIO.setup(PIN_ECHO2, GPIO.IN)

client = mqtt.Client()

# Callback when the client receives a CONNACK response from the server
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(CONTROL_TOPIC)

client.on_connect = on_connect

client.connect(BROKER, PORT, 60)
client.loop_start()

def get_distance(trigger_pin, echo_pin):
    GPIO.output(trigger_pin, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(trigger_pin, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trigger_pin, GPIO.LOW)

    while GPIO.input(echo_pin) == 0:
        pulse_start_time = time.time()

    while GPIO.input(echo_pin) == 1:
        pulse_end_time = time.time()

    pulse_duration = pulse_end_time - pulse_start_time
    distance = round(pulse_duration * 17150, 2)
    return distance

try:
    while True:
        try:
            humidity = DHT_SENSOR.humidity
            temperature = DHT_SENSOR.temperature
        except RuntimeError as error:
            # Handle occasional sensor read errors
            print(f"Error reading DHT22 sensor: {error}")
            time.sleep(2.0)
            continue

        # Read distance from the first ultrasonic sensor
        distance1 = get_distance(PIN_TRIGGER1, PIN_ECHO1)
        print("Distance from sensor 1:", distance1, "cm")

        if distance1 < 30:
            print("Water Level Exceeded")
            client.publish(CONTROL_TOPIC, json.dumps({"action": "deactivate"}))

        # Read distance from the second ultrasonic sensor
        distance2 = get_distance(PIN_TRIGGER2, PIN_ECHO2)
        print("Distance from sensor 2:", distance2, "cm")

        sensor_data = {
            "temperature": temperature,
            "humidity": humidity,
            "distance1": distance1,
            "distance2": distance2,
            "image": None,  # No image
        }

        client.publish(DATATOPIC, json.dumps(sensor_data))
        print(f"Published data: {sensor_data}")

        if humidity > 80:
            client.publish(CONTROL_TOPIC, json.dumps({"action": "activate"}))
            print("Motor activation message sent")
            # send WhatsApp message through Twilio API

        time.sleep(10)

except KeyboardInterrupt:
    print("Exiting...")
    client.loop_stop()
    client.disconnect()
    GPIO.cleanup()
