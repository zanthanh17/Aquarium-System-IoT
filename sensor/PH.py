from machine import Pin, ADC, SoftI2C

adc = ADC(Pin(34))
# ADC attenuation and width setting (for 0-3.3V range)
adc.atten(ADC.ATTN_11DB)  # Full range: 3.3

def read_ph():  

    avgValue = adc.read()
    phVol = avgValue * (3.3 / 4095)
    phValue = 3.3 * phVol  # Tính pH
    if phValue < 0 or phValue > 14:  # Kiểm tra pH
        print("Error: pH value out of range.")
    print('VOLTAGE: {:.2f} V'.format(phVol), 'PH: {:.2f}'.format(phValue))
    return phValue 

