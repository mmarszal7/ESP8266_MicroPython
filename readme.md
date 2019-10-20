# ESP8266 - with [MicroPython]

https://github.com/nodemcu/nodemcu-devkit-v1.0

https://docs.micropython.org/en/latest/esp8266/esp8266/quickref.html

http://micropython.org/webrepl/?

---
# [WEB REPL]

1. Check NodeMCU port
2. Use WEB REPL - just go to http://micropython.org/webrepl/ and connect to 192.168.0.14:8266
3. Prototyping: paste script code into REPL or rename script to 'main.py' and send it to the device
4. To run script from file run _import script.py_

--- 
## First time(!) configuration - running WEB REPL

1.  Download serial port tool (e.g. [TeraTerm] or Ptty) - speed 115200
2.  Connect to proper COM (serial port with hardware)
3.  Connect to your local web. Change connection type from 'Access point' (AP) to 'Station' (STA):

        ```python
        >>> import network
        >>> sta_if = network.WLAN(network.STA_IF)
        >>> ap_if = network.WLAN(network.AP_IF)

        # connection
        >>> ap_if.active(False)
        >>> sta_if.connect('network_name', 'password')
        >>> sta_if.isconnected()
        >>> sta_if.ifconfig()
        ('192.168.0.14', '255.255.255.0', '192.168.0.1', '8.8.8.8')
        ```

4.  Run _import webrepl_setup_ and follow the on-screen instructions
5.  Go to [WEB REPL] and connect to NodeMCU (192.168.0.14:8266). Add do_connect() to boot.py:

        ```python
        def do_connect():
        import network
        sta_if = network.WLAN(network.STA_IF)
        if not sta_if.isconnected():
            print('connecting to network...')
            sta_if.active(True)
            sta_if.connect('<essid>', '<password>')
            while not sta_if.isconnected():
                pass
        print('network config:', sta_if.ifconfig())
        ```
        
## Firmware update

1. Download NodeMCU [Flasher]
2. Download new Firmware (e.g. [MicroPython])
3. Flash firmware with NodeMCU Flasher (first read [Flasher] instruction)

[flasher]: https://github.com/nodemcu/nodemcu-flasher#nodemcu-flasher
[micropython]: https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/intro.html
[teraterm]: https://ttssh2.osdn.jp/index.html.en
[web repl]: http://micropython.org/webrepl/
[micropython]: https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/intro.html
