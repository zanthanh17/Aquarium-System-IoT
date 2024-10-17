from machine import Pin

# motor1 = Pin(12, Pin.OUT)
# motor2 = Pin(14,Pin.OUT)

def Pump(temp, NTU , phValue, levels):
    if (temp > 31 or NTU > 500 or  phValue > 7 or levels == True):
        print("MOTOR ON")  # Bật động cơ
        # motor1.on()
    else:
        print("MOTOR OFF")  # Tắt động cơ
        # motor2.off()

def flush(level):
    if level:
        print('Xa nuoc')
        # motor2.on()
    else: 
        print('OFF') 
        # motor2.off()



