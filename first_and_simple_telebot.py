import os
import telebot
from flask import Flask
import threading

TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN') or os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

# Tera channel / group
CHANNEL_ID = "@Kollywood_king_request_bot"

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Bot Live hai ✅")

@bot.message_handler(func=lambda m: True)
def all_msg(message):
    try:
        # Channel me forward
        text = f"User: {message.from_user.first_name}\nMsg: {message.text}"
        bot.send_message(CHANNEL_ID, text)
    except Exception as e:
        print(e)
    bot.reply_to(message, "Ho gaya 👍")

# Flask for Render Live
app = Flask(__name__)
@app.route('/')
def home():
    return "Bot Running"

def run_flask():
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))

threading.Thread(target=run_flask, daemon=True).start()
bot.infinity_polling()
