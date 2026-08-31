import os
import requests
from datetime import datetime
import pytz
from dotenv import load_dotenv
import time

load_dotenv()
IST = pytz.timezone('Asia/Kolkata')

# Render me variable ka naam TELEGRAM_AUTH_TOKEN rakhna
telegram_auth_token = os.getenv("TELEGRAM_AUTH_TOKEN") 
telegram_group_id = "@Date_and_time_notifier" # @ lagaya

def send_msg_on_telegram(message):
    telegram_api_url = f"https://api.telegram.org/bot{telegram_auth_token}/sendMessage?chat_id={telegram_group_id}&text={message}"
    tel_resp = requests.get(telegram_api_url)
    print(tel_resp.text) # isse asli error dikhega
    if tel_resp.status_code == 200:
        print("INFO : Notification sent")
    else:
        print("ERROR: Could not send Message")

# Loop me daal diya taki Render band na kare
while True:
    raw_TS = datetime.now(IST)
    curr_date = raw_TS.strftime("%d-%m-%Y")
    curr_time = raw_TS.strftime("%H:%M:%S")
    msg = f"Message received on {curr_date} at {curr_time}"
    send_msg_on_telegram(msg)
    time.sleep(3600) # 1 ghante me 1 baar bhejega
