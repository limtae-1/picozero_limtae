from picozero import DHTSensor
from time import sleep

dht_sensor = DHTSensor(pin=0, model='DHT11')

# Print the temperature and humidity
while True:
    print(dht_sensor.temperature)
    sleep(1)
    #print(type(dht_sensor.temperature))
    print(dht_sensor.humidity)
    sleep(1)
    print("=======")
