from machine import Pin, ADC, SoftI2C

def read_turbidity():
    adc = ADC(Pin(35))
    adc.atten(ADC.ATTN_11DB)
    Volt = 0
    Volt = adc.read() / 4095 * 5  # Chuyển đổi giá trị đọc từ ADC thành điện áp (5V tham chiếu)
    
    # Lấy trung bình 800 lần đọc để giảm nhiễu
    for _ in range(800):
        Volt += (adc.read() / 4095) * 5
    Volt /= 800

    if Volt < 2.5:
        NTU = 3000
    elif Volt > 4.2:
        NTU = 0
    else:
        NTU = -1120.4 * Volt * Volt + 5742.3 * Volt - 4352.9
    print('VOLTAGE: {:.2f} V'.format(Volt) , 'TURBIDITY: {:.2f} NTU'.format(NTU))
    return NTU