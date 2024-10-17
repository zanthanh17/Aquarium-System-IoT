from machine import Pin, ADC

adc = ADC(Pin(34))
# ADC attenuation and width setting (for 0-3.3V range)
adc.atten(ADC.ATTN_11DB)  # Full range: 3.3
adc.width(ADC.WIDTH_12BIT)  # Độ phân giải 12-bit (giá trị từ 0-4095)

def read_ph():  

    adc_value = adc.read()  # Đọc giá trị ADC
    voltage = adc_value * 3.3 / 4095  # Chuyển đổi giá trị ADC sang điện áp 0-3.3V
    ph = 20.5940-5.4450*voltage  # Công thức tính pH dựa trên điện áp
    # if ph < 0 or ph > 14:  # Kiểm tra pH
    #     print("Error: pH value out of range.")
    print('VOLTAGE: {:.2f} V'.format(voltage), 'PH: {:.2f}'.format(ph))
    return ph 

