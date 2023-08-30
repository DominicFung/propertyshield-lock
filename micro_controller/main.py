from mfrc522 import MFRC522 
import utime
import machine

import time
import ubinascii
from umqtt.simple import MQTTClient
import random

# Default  MQTT_BROKER to connect to
MQTT_BROKER = "192.168.100.22"
CLIENT_ID = ubinascii.hexlify(machine.unique_id())
SUBSCRIBE_TOPIC = b"led"
PUBLISH_TOPIC = b"temperature"

# Setup built in PICO LED as Output
led = machine.Pin("LED",machine.Pin.OUT)

# Publish MQTT messages after every set timeout
last_publish = time.time()
publish_interval = 5

lock = machine.Pin(28, machine.Pin.OUT)
buzzer = machine.Pin(27, machine.Pin.OUT)
RLed = machine.Pin(18, machine.Pin.OUT)
GLed =machine.Pin(19, machine.Pin.OUT)

lock.value(1)
buzzer.value(0)
RLed.value(0)
GLed.value(0)

# https://iotprojectsideas.com/rfid-based-door-lock-control-system-using-raspberry-pi-pico/

def uidToString(uid):
    mystring = ""
    for i in uid:
        mystring = "%02X" % i + mystring
    return mystring
                  
rc522 = MFRC522(spi_id=0,sck=6,miso=4,mosi=7,cs=5,rst=22)

# Publish MQTT messages after every set timeout
last_publish = time.time()
publish_interval = 5

# Received messages from subscriptions will be delivered to this callback
def sub_cb(topic, msg):
    print((topic, msg))
    if msg.decode() == "ON":
        led.value(1)
    else:
        led.value(0)


def reset():
    print("Resetting...")
    time.sleep(5)
    machine.reset()
    
# Generate dummy random temperature readings    
def get_temperature_reading():
    return random.randint(20, 50)
    
def main():
    print(f"Begin connection with MQTT Broker :: {MQTT_BROKER}")
    mqttClient = MQTTClient(CLIENT_ID, MQTT_BROKER, keepalive=60)
    mqttClient.set_callback(sub_cb)
    mqttClient.connect()
    mqttClient.subscribe(SUBSCRIBE_TOPIC)
    print(f"Connected to MQTT  Broker :: {MQTT_BROKER}, and waiting for callback function to be called!")
    while True:
            # Non-blocking wait for message
            mqttClient.check_msg()
            global last_publish
            if (time.time() - last_publish) >= publish_interval:
                random_temp = get_temperature_reading()
                mqttClient.publish(PUBLISH_TOPIC, str(random_temp).encode())
                last_publish = time.time()
            time.sleep(1)


if __name__ == "__main__":
    while True:
        try:
            main()
        except OSError as e:
            print("Error: " + str(e))
            reset()

print("")
print("Place the RFID Card")
print("")


while True:

    (stat, tag_type) = rc522.request(rc522.REQALL)

    if stat == rc522.OK:
        (status, raw_uid) = rc522.SelectTagSN()
        if stat == rc522.OK:
            rfid_data = "{:02x}{:02x}{:02x}{:02x}".format(raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])
            print("Card detected! UID: {}".format(rfid_data))
            if rfid_data == "81a3dc79":
                
                lock.value(0)
                GLed.value(1)
                utime.sleep(5)
                lock.value(1)
                GLed.value(0)
                
                
            elif rfid_data == "ad6d1583":
                
                lock.value(0)
                GLed.value(1)
                utime.sleep(5)
                lock.value(1)
                GLed.value(0)
                
            elif rfid_data == "866080f8":
                
                lock.value(0)
                GLed.value(1)
                utime.sleep(5)
                lock.value(1)
                GLed.value(0)
                
                
            elif rfid_data == "337cd633":
                
                lock.value(0)
                GLed.value(1)
                utime.sleep(5)
                lock.value(1)
                GLed.value(0)
                

            else:
                
                buzzer.value(1)
                RLed.value(1)
                utime.sleep(1)
                buzzer.value(0)
                RLed.value(0)