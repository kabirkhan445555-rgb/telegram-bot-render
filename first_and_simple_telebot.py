import os
from flask import Flask
import threading
import telebot

TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
if not TOKEN:
    print("ERROR: TELEGRAM_BOT_TOKEN missing")
    exit(1)

bot = telebot.TeleBot(TOKEN)
telegram_group_id = "@Kollywood_king_request_bot"

@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, "Bot Live hai da ✅")

@bot.message_handler(func=lambda m: True)
def echo(m):
    try:
        bot.send_message(telegram_group_id, f"New msg from {m.from_user.first_name}: {m.text}")
    except:
        pass
    bot.reply_to(m, f"You said: {m.text}")

app = Flask(__name__)
@app.route('/')
def home():
    return "Bot Running"

def run_bot():
    bot.infinity_polling()

def run_flask():
    app.run(host='0.0.0.0', port=10000)

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    run_flask()
