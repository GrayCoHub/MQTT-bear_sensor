import sys
import paho.mqtt.client as mqtt

# from typing import Literal

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    # Define a fallback for Literal or use a third-party library like typing_extensions.
    from typing_extensions import Literal

def handle_status(status: Literal['open', 'closed']):
    print(f"Handling a {status} status")

handle_status('open')  # This is fine
handle_status('closed')  # This is also fine
handle_status('pending')  # This would raise a type error with static type checkers like mypy

# Callback when connecting to the MQTT server
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribe to the topic here
    client.subscribe("bear_sensor")

# Callback when receiving a message from the subscribed topic
def on_message(client, userdata, msg):
    print(f"Received message '{msg.payload.decode()}' on topic '{msg.topic}'")

# Initialize and configure the MQTT client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT server (update host to your MQTT server)
client.connect("broker.mqtt-dashboard.com", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks, and handles reconnecting.
client.loop_forever()