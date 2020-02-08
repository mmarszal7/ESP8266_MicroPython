import machine
import dht
import urequests
import time

# DHT is on pin 14 (D5 - check pinout)
d = dht.DHT11(machine.Pin(14))
host = 'http://192.168.0.39:80/grafana/index.php?'

while True:
    d.measure()
    
    params = 'temperature={0}&humidity={1}'.format(d.temperature(), d.humidity())
    response = urequests.get(host + params)
    response.close()
    
    print(params)
    time.sleep(3)
