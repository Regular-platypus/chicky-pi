import supervisor
import time
import digitalio
from board import *
import board
from duckyinpython import *
import wifi

time.sleep(.5)

def startWiFi():
    import ipaddress
    try:
        from secrets import secrets
    except ImportError:
        raise
    wifi.radio.start_ap(secrets['ssid'],secrets['password'])
    HOST = repr(wifi.radio.ipv4_address_ap)
    PORT = 80

progStatus = False
progStatus = getProgrammingStatus()
print("progStatus", progStatus)
if(progStatus == False):
    payload = selectPayload()
    runScript(payload)
else:
    print("no payload")

