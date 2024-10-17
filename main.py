import network
import time
import device.oled as oled
import Data.blynk_cloud as blynk_cloud
import sensor.turbidity as TUR
import sensor.Temp as Temp
import sensor.PH as ph
import Data.ggsheet as ggsheet
import device.servo as servo
import device.check_control as motor
import sensor.levelwater as levelwater

"""
    nhietdo d4
    ph 34
    ntu 35
    servo 2
    muc nuoc 16
    dong co   
"""

# ket noi wifi
def connect_WIFI():
    ssid = 'Giangvien'
    password ='dhbk@2024'
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(ssid, password)
    while not station.isconnected():
        print('Connecting to WiFi...')
        time.sleep(1)
    print('WiFi connected to:', ssid)
    print(station.ifconfig())

connect_WIFI()
# Cau hinh blynk
blynk = blynk_cloud.blynklib_mp.Blynk("4Sly-C35Dvbbi8FWkc9mmCpMfGfK0NJl")
blynk_cloud.connect_blynk(blynk)

while True:             
    # Goi ham cac gia tri cam bien
    NTU = TUR.read_turbidity()
    phValue = ph.read_ph() 
    temp = Temp.read_temperature()
    level = levelwater.water_level()
    
    # set cac gia tri nguong~
    thresholds = motor.standard_value(26,500,7)

    # so sanh nguong va dieu khien dong co bom nuoc
    # motor.Pump(thresholds,NTU)

    # dieu khien dong co xa nuoc
    motor.flush(level)

    #kiem tra thoi gian cho ca an
    servo_status = servo.check_and_feed()
    if servo_status:
        status = 'ON'        #6a.m & 6p.m thi trang thai servo ON
    else: status = 'OFF'     #cac time khac thi servo OFF

    #hien thi gia tri len oled
    oled.oled_display(thresholds,temp,NTU,phValue)

    # # hien thi gia tri len Blynk cloud
    blynk_cloud.display_blynk(blynk,temp,NTU,phValue)

    # hien thi gia tri len google sheet
    ggsheet.get_data(status,temp,NTU,phValue)
            
    time.sleep(2)


