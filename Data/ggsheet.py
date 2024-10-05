import urequests
import ntptime
import time

ntptime.host = 'pool.ntp.org'  # Use this or another known NTP server

server_url = 'https://script.google.com/macros/s/AKfycbxRFCwRGGV5haYvg22C61vgGLbLgjdrVheQWW5v2DzSOqUWdI6QtHui1RvNdVnXuA-X/exec'

def get_ntp_time():
    try:
        ntptime.settime()  # Synchronize the system time with NTP
        tm = time.localtime(time.time())  # Get local time
        formatted_time = "{:02d}:{:02d}:{:02d}".format(tm[3] + 7, tm[4], tm[5])
        return formatted_time
    except Exception as e:
        print("Error getting NTP time:", e)
        return None
    
def get_data(status,NTU,phValue):
    timestamp = get_ntp_time()
    # Prepare JSON payload
    json_data = {
        "method": "append",
        # "temp": temp;
        "NTU": NTU,
        "phValue": phValue,
        "status": status,
        "timestamp": timestamp,
    }
    # Send HTTP POST request
    try:
        response = urequests.post(server_url, json=json_data)
        print("Response:", response.status_code, response.text)
        response.close()
    except Exception as e:
        print("Error sending data:", e)