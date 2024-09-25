from machine import Pin, ADC, SoftI2C

def read_ph():
    adc = ADC(Pin(34))
    buf = [adc.read() for _ in range(10)]
    buf.sort()
    avgValue = sum(buf[2:8]) / 6
    phVol = avgValue * 3.3 / 4095 / 4.3
    phValue = 14.2 - (-5.70 * phVol + 29.5)
    print('PH: {:.2f}'.format(phValue))
    return phValue 