import socket
import machine

# Led on pin D1
# Change state by GET: http://192.168.0.14:8080/off
led = machine.Pin(5, machine.Pin.OUT)
led.value(1)

def getCommand(response):
    response = response.decode("utf-8")
    start = response.find(" ")
    end = response.find(" ", start+1)
    
    return(response[start+1:end])

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
        cmd = getCommand(req)
        print(cmd)

        if (cmd == "/on"):
            led.value(0)
        elif (cmd == "/off"):
            led.value(1)
        
        client_s.close()

main()