import os
from flask import Flask
import threading
import telebot

TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
if not TOKEN:
    print("ERROR: TELEGRAM_BOT_TOKEN missing")
    exit(1)

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, "Bot Live hai da ✅")

@bot.message_handler(func=lambda m: True)
def echo(m):
    bot.reply_to(m, f"You said: {m.text}")

app = Flask(__name__)
@app.route('/')
def home():
    return "Bot is running!"

def run_bot():
    print("Bot polling started...")
    bot.infinity_polling()

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
