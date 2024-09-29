from machine import Pin, ADC, SoftI2C
import onewire
import ds18x20
import time

def read_temperature():
    dat = Pin(4)
    ds_sensor = ds18x20.DS18X20(onewire.OneWire(dat))
    roms = ds_sensor.scan()
    print('Found DS18B20 devices: ', roms)
    if not roms:
        print("No DS18B20 devices found!")
    ds_sensor.convert_temp()
    time.sleep_ms(750)
    for rom in roms:
        temp = ds_sensor.read_temp(rom)
        print('Temperature: {:.2f} C'.format(temp))
        return temp