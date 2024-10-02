from machine import Pin, ADC, SoftI2C

def read_turbidity():
    adc = ADC(Pin(35))
    adc.atten(ADC.ATTN_11DB)
    Volt = 0
    Volt = adc.read() / 4095 * 5  # Chuyển đổi giá trị đọc từ ADC thành điện áp (5V tham chiếu)
    
    # Lấy trung bình 800 lần đọc để giảm nhiễu
    for _ in range(800):
        Volt += (adc.read() / 4095) * 3.3
    Volt /= 800

    if Volt < 0.36:
        NTU = 3000
    elif Volt > 1.8:
        NTU = 0
    else:
        NTU = (-1120.4 * (Volt + 2.4) ** 2 + 5742.3 * (Volt + 2.4) - 4352.9)
    print('VOLTAGE: {:.2f} V'.format(Volt) , 'TURBIDITY: {:.2f} NTU'.format(NTU))
    return NTU