from machine import Pin,PWM
import time
import Data.ggsheet as data

servo_pin = Pin(2)  # Chọn chân GPIO phù hợp
servo = PWM(servo_pin, freq=50)

def feed_fish():
    print("Servo ON")
    servo.duty(77)  # Mở servo
    time.sleep(3)  # Đợi 5 giây
    servo.duty(26)  # Đóng servo
    print("Servo OFF")

def check_and_feed():
    current_time = data.get_ntp_time()
    if current_time:
        hour, minute, second = map(int, current_time.split(':'))
    else: return False

    if (hour == 16 and minute == 41 and 0 <=second <= 30) or (hour == 18 and minute == 0):
        feed_fish()
        return True  
    else: return False