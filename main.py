from machine import Pin, ADC, SoftI2C
import network
import time
import math
import sensor_and_device.oled as oled
import blynk_cloud.blynk_cloud as blynk_cloud
import sensor_and_device.turbidity as TUR
import sensor_and_device.Temp as Temp
import sensor_and_device.PH as ph
import ggsheet.data as data
import sensor_and_device.servo as servo

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

# blynk = blynk_cloud.blynklib_mp.Blynk("4Sly-C35Dvbbi8FWkc9mmCpMfGfK0NJl")
# blynk_cloud.connect_blynk(blynk)

while True:               
    NTU = TUR.read_turbidity()
    phValue = ph.read_ph() 
    # temp = Temp.read_temperature()

    servo_status = servo.check_and_feed()

    if servo_status:
        status = 'ON'
    else: status = 'OFF'


    # oled.oled_display(NTU,phValue)

    # blynk_cloud.display_blynk(blynk,NTU,phValue)

    data.get_data(NTU,phValue,status)
            
    time.sleep(2)


