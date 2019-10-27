import machine
import time

# ADC is on pin 0 (A0)
adc = machine.ADC(0)

while True:
    value = adc.read()
    
    print(value)
    time.sleep(0.5)
