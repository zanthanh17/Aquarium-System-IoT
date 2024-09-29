from machine import Pin,PWM
import time
import ggsheet.data as data

servo_pin = Pin(15)  # Chọn chân GPIO phù hợp
servo = PWM(servo_pin, freq=50)

def set_servo_angle(angle):
    duty = int((angle / 180) * 1023 + 26)
    servo.duty(duty)

def feed_fish():
    print("Servo ON")
    set_servo_angle(90)  # Mở servo
    time.sleep(5)  # Đợi 5 giây
    set_servo_angle(0)  # Đóng servo
    print("Servo OFF")

def check_and_feed():
    current_time = data.get_ntp_time()
    if current_time:
        hour, minute = map(int, current_time.split(':')[:2])
    if (hour == 6 and minute == 24) or (hour == 18 and minute == 0):
        feed_fish()
        return True   
    else: return False