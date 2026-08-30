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
def all_messages(m):
    try:
        bot.send_message(telegram_group_id, f"New msg from {m.from_user.first_name}: {m.text}")
    except Exception as e:
        print(f"Channel send fail (bot admin nahi hai): {e}")
    bot.reply_to(m, "Message mil gaya 👍")

app = Flask(__name__)
@app.route('/')
def home():
    return "Bot is running"

def run_flask():
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))

threading.Thread(target=run_flask).start()
print("Bot polling started...")
bot.infinity_polling()
