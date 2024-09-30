from machine import Pin

motor = Pin(2, Pin.OUT)

def standard_value(std_temp,std_phValue,std_NTU):
    return {
    'temperature': std_temp,  # Nhiệt độ (°C)
    'turbidity': std_NTU,     # Độ đục (NTU)
    'pH': std_phValue,          # Độ pH
    }

def check_and_control_motor(thresholds, temperature, turbidity, ph_value, water_level):
    
    
    if (temperature > thresholds["temp"] or
        turbidity > thresholds["turbidity"] or
        thresholds["ph" - 0.5] <= ph_value >= thresholds["ph" + 1] or
        water_level > thresholds["water_level"]):
        motor.on()  # Bật động cơ
    else:
        motor.off()  # Tắt động cơ


