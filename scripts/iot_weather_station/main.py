import machine
import dht
import urequests
import time

# DHT is on pin 2 (D4)
d = dht.DHT11(machine.Pin(4))
host = 'http://192.168.0.39/grafana/index.php?'

while True:
    d.measure()
    
    params = 'temperature={0}&humidity={1}'.format(d.temperature(), d.humidity())
    response = urequests.get(host + params)
    response.close()
    
    print(params)
    time.sleep(3)
