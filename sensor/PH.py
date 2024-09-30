from machine import Pin, ADC, SoftI2C

adc = ADC(Pin(8))
# ADC attenuation and width setting (for 0-3.3V range)
adc.atten(ADC.ATTN_11DB)  # Full-scale voltage: 3.3V
adc.width(ADC.WIDTH_12BIT)  # 12-bit resolution, value range: 0-4095


def read_ph():  
    buf = [adc.read() for _ in range(10)]
    buf.sort()
    avgValue = sum(buf[2:8]) / 6
    phVol = avgValue * 3.3 / 4095 / 4.3
    phValue = 7 + ((2.5 - phVol) / 0.167)  # Tính pH
    if phValue < 0 or phValue > 14:  # Kiểm tra pH
        print("Error: pH value out of range.")
        return None
    print('VOLTAGE: {:.2f} V'.format(phVol), 'PH: {:.2f}'.format(phValue))
    return phValue 

