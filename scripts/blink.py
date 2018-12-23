from machine import Pin
import time

p_out = Pin(5, Pin.OUT)

while True:
    p_out.on()
    time.sleep(1)     
    p_out.off()
    time.sleep(1)    
