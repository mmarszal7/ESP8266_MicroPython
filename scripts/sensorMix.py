'''
Script that allows you to measure temperature, humidity and illuminance
(DHT11, photoresistor, 10kOhm resistor, led with resistor)

Temp & Humidity - 3.3V / pin D2 / - / GND
Illuminance - valtage on divider (10kOhm + photo) on pin A0 
LED - pin D1
'''
from machine import Pin
from machine import ADC
import dht
import machine
import time
import temperature_sensor
import photo_resistor

led = Pin(5, Pin.OUT)
sensor = dht.DHT11(machine.Pin(4))
adc = ADC(0)

def readTemperature():
    sensor.measure()
    print("Temperature: {} C".format(sensor.temperature()))
    print("Humidity: {} %".format(sensor.humidity()))
    
def readIlluminance():
    illuminance = adc.read()
    print("Illuminance: {} %".format(illuminance))
    return illuminance

def main():
    while True:
        readTemperature()
        illuminance = readIlluminance(adc)
        if(illuminance < 300):
            led.on()
        else:
            led.off()
        time.sleep(1)    
        
main()