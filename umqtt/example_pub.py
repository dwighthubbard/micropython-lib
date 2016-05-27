import time
from umqtt import MQTTClient

# Test reception e.g. with:
# mosquitto_sub -t foo_topic

c = MQTTClient("umqtt_client", "localhost")
c.connect()
c.publish(b"foo_topic", b"hello")
c.disconnect()
