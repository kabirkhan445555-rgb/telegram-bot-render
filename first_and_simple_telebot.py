import pytz
from datetime import datetime
import requests
from dotenv import load_dotenv
import os

IST = pytz.timezone('Asia/Kolkata')
raw_TS = datetime.now(IST)
curr_date = raw_TS.strftime("%d-%m-%Y")
curr_time = raw_TS.strftime("%H:%M:%S")

load_dotenv()
telegram_auth_token = os.getenv("TELEGRAM_BOT_TOKEN") or os.getenv("BOT_TOKEN")

# Yaha @ ke saath daal
telegram_group_id = "@Date_and_time_notifi" 

msg = f"Message received on {curr_date} at {curr_time}"

def send_msg_on_telegram(message):
    telegram_api_url = f"https://api.telegram.org/bot{telegram_auth_token}/sendMessage?chat_id={telegram_group_id}&text={message}"
    try:
        response = requests.get(telegram_api_url)
        print(response.text)
        if response.status_code != 200:
            print(f"ERROR: {response.text}")
        else:
            print("Message sent successfully")
    except Exception as e:
        print(f"ERROR: {e}")

# Ek baar hi bhejo
if __name__ == "__main__":
    send_msg_on_telegram(msg)
