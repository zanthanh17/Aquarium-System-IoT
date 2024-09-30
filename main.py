import network
import time
import math
import device.oled as oled
import Data.blynk_cloud as blynk_cloud
import sensor.turbidity as TUR
import sensor.Temp as Temp
import sensor.PH as ph
import Data.ggsheet as ggsheet
import device.servo as servo
import device.check_control as motor

def connect_WIFI():
    ssid = 'NHATRO BM T1'
    password ='nhatro123456t1'
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(ssid, password)
    while not station.isconnected():
        print('Connecting to WiFi...')
        time.sleep(1)
    print('WiFi connected to:', ssid)
    print(station.ifconfig())

blynk = blynk_cloud.blynklib_mp.Blynk("4Sly-C35Dvbbi8FWkc9mmCpMfGfK0NJl")
blynk_cloud.connect_blynk(blynk)

connect_WIFI()
while True:               
    NTU = TUR.read_turbidity()
    phValue = ph.read_ph() 
    temp = Temp.read_temperature()

    # set cac gia tri nguong~
    thresholds = motor.standard_value(temp_threshold=30, turbidity_threshold=500,ph_threshold = 7)
    # so sanh nguong va dieu khien dong co bom nuoc
    motor.check_and_control_motor(thresholds,temp,NTU,phValue)

    # kiem tra thoi gian cho ca an
    servo_status = servo.check_and_feed()
    if servo_status:
        status = 'ON'        #6a.m & 6p.m thi trang thai servo ON
    else: status = 'OFF'     #cac time khac thi servo OFF

    oled.oled_display(thresholds,NTU,phValue)

    blynk_cloud.display_blynk(blynk,NTU,phValue)

    ggsheet.get_data(status)
            
    time.sleep(1)


