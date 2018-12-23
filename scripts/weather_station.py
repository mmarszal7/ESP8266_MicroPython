import socket
import machine
import dht

CONTENT = b"""\
HTTP/1.0 200 OK
<h1>Micropython weather station</h1>
<p>Temperature: {0} °C</p>
<p>Humidity: {1}%</p>
"""

# DHT is on pin 2 (D4)
d = dht.DHT11(machine.Pin(4))

def main():
    s = socket.socket()
    ai = socket.getaddrinfo("192.168.0.14", 8080)
    addr = ai[0][-1]
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(addr)
    s.listen(5)
    print("Listening, connect your browser to http://192.168.0.14:8080/")

    while True:
        res = s.accept()
        client_s = res[0]
        client_addr = res[1]
        req = client_s.recv(1024)
        print(req)

        d.measure()
        
        client_s.send(CONTENT.format(d.temperature(), d.humidity()))
        client_s.close()

main()