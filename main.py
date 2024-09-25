from machine import Pin, ADC, SoftI2C
import sh1106
import blynklib_mp
import urequests
import ntptime
import network
import time
import math
import sensor.turbidity as TUR
import sensor.Temp as Temp
import sensor.PH as ph
# import ggsheet.data as data

i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=400000)
display = sh1106.SH1106_I2C(128, 64, i2c, Pin(16), 0x3c)

ssid = 'NHATRO BM T1'
password = 'nhatro123456t1'
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)
while not station.isconnected():
    print('Connecting to WiFi...')
    time.sleep(1)
print('WiFi connected to:', ssid)
print(station.ifconfig())

BLYNK_TEMPLATE_ID = "TMPL6Z78zEeyN"
BLYNK_TEMPLATE_NAME = "PBL3"
BLYNK_AUTH_TOKEN = "ntlI3mfVTq7OGbENwVtmV6VG89xuipbK"
blynk = blynklib_mp.Blynk("4Sly-C35Dvbbi8FWkc9mmCpMfGfK0NJl")
if blynk is None:
    print('Failed to initialize Blynk')
else:
    print('Blynk initialized successfully')

ntptime.host = 'pool.ntp.org'  # Use this or another known NTP server

server_url = 'https://script.google.com/macros/s/AKfycbwEBDMV7npCrkxAaN1BUHYQaHLqwUZRsOI8U5uhgOT5i89fABizurx9U6Zq6vz7RizY/exec'

def get_ntp_time():
    try:
        ntptime.settime()  # Synchronize the system time with NTP
        tm = time.localtime(time.time())  # Get local time
        formatted_time = "{:02d}:{:02d}:{:02d}".format(tm[3], tm[4], tm[5])
        return formatted_time
    except Exception as e:
        print("Error getting NTP time:", e)
        return None

while True:               
    NTU = TUR.read_turbidity()
    phValue = ph.read_ph() 
    # temp = Temp.read_temperature()
        
    display.fill(0)
    display.text("Tur: {:.2f} NTU".format(NTU), 0, 0) 
    display.text("PH: {:.2f}".format(phValue), 0, 15) 
    # display.text("Temp: {:.2f} C".format(temp), 5, 30)
    display.show()

    if blynk is not None:
        blynk.virtual_write(1,NTU)
        blynk.virtual_write(2,phValue)
        # blynk.virtual_write(0,temp)
        blynk.run()
    # Get current time
    # data.get_data()
    timestamp = get_ntp_time()
    # Prepare JSON payload
    json_data = {
        "method": "append",
        # "temp": temp,
        "NTU": NTU,
        "phValue": phValue,
        "timestamp": timestamp,
    }
    # Send HTTP POST request
    try:
        response = urequests.post(server_url, json=json_data)
        print("Response:", response.status_code, response.text)
        response.close()
    except Exception as e:
        print("Error sending data:", e)
            
    time.sleep(2)


