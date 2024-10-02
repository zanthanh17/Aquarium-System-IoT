from machine import Pin, ADC, SoftI2C
import lib.sh1106 as sh1106

i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=400000)
display = sh1106.SH1106_I2C(128, 64, i2c, Pin(16), 0x3c)

def oled_display(thresholds,NTU,phValue):
    display.fill(0)
    # display.text("Temp: {:.2f}C".format(temp), 0, 0)
    # display.text("Thresh: {}C".format(thresholds["temp"]), 64, 0)S
    display.text("Turb:{:.2f}".format(NTU), 0, 16)
    display.text("|{:.}".format(thresholds["turbidity"]), 86, 16)
    display.text("pH:{:.}".format(phValue), 0, 32)
    display.text("|{:.}".format(thresholds["pH"]), 64, 32)
    display.show()