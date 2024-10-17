from machine import Pin

# motor1 = Pin(12, Pin.OUT)
# motor2 = Pin(14,Pin.OUT)

def standard_value(std_temp,std_NTU,std_phValue):
    return {
    'temp': std_temp,  # Nhiệt độ (°C)
    'turbidity': std_NTU,     # Độ đục (NTU)
    'pH': std_phValue,          # Độ pH
    }

# def Pump(thresholds, turbidity):
#     if turbidity > thresholds["turbidity"] :
#         print("MOTOR ON")  # Bật động cơ
#         # motor1.on()
#     else:
#         print("MOTOR OFF")  # Tắt động cơ
#         # motor2.off()

def flush(level):
    if level:
        print('Xa nuoc')
        # motor2.on()
    else: 
        print('OFF') 
        # motor2.off()



