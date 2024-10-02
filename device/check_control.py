from machine import Pin

# motor = Pin(5, Pin.OUT)

def standard_value(std_NTU,std_phValue):
    return {
    # 'temperature': std_temp,  # Nhiệt độ (°C)
    'turbidity': std_NTU,     # Độ đục (NTU)
    'pH': std_phValue,          # Độ pH
    }

def check_and_control_motor(thresholds, turbidity, ph_value):
    
    if turbidity > thresholds["turbidity"] or ph_value > thresholds["pH"]:
        print("MOTOR ON")  # Bật động cơ
    else:
        print("MOTOR OFF")  # Tắt động cơ


