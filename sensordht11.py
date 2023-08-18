import board
import adafruit_dht
import time

# Set up the DHT11 sensor
dht_pin = board.D4  # Set the pin where the DHT11 data pin is connected to GPIO 4
dht_sensor = adafruit_dht.DHT11(dht_pin)

try:
    while True:
        try:
            temperature = dht_sensor.temperature
            humidity = dht_sensor.humidity
            if temperature is not None and humidity is not None:
                print('Temperature: {:.1f}°C, Humidity: {:.1f}%'.format(temperature, humidity))
                print("================================================================")
            else:
                print('Data not available.')
        except RuntimeError as e:
            print('Error reading from sensor:', e)

        time.sleep(1)

except KeyboardInterrupt:
    pass