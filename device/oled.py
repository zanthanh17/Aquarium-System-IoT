from machine import Pin, ADC, SoftI2C
import lib.sh1106 as sh1106

i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=400000)
display = sh1106.SH1106_I2C(128, 64, i2c, Pin(16), 0x3c)

def oled_display(temp,NTU,phValue):
    display.fill(0)
    display.text("Temp:{:d}°C | 26°C".format(int(temp)), 0, 0)
    display.text("Turb:{:.2f} | 500 NTU".format(NTU), 0, 16)
    display.text("pH:{:.2f} | 7".format(phValue), 0, 32)
    display.show()