from machine import Pin, ADC

PinWater = Pin(15, Pin.IN)

def water_level():
    valor = PinWater.value()
    if valor == 0:
        return True
    else: return False
