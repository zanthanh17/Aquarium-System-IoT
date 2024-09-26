from machine import Pin, ADC, SoftI2C
import sh1106

i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=400000)
display = sh1106.SH1106_I2C(128, 64, i2c, Pin(16), 0x3c)

def oled_display(NTU, phValue):
    display.fill(0)
    display.text("Tur: {:.2f} NTU".format(NTU), 0, 0) 
    display.text("PH: {:.2f}".format(phValue), 0, 15) 
    # display.text("Temp: {:.2f} C".format(temp), 5, 30)
    display.show()