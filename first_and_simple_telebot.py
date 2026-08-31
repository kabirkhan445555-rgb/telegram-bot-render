import os
import telebot
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Bot Live hai! Render pe chal raha hai.")

@bot.message_handler(func=lambda m: True)
def reply(message):
    bot.reply_to(message, f"Aapne bola: {message.text}")

print("Bot starting...")
bot.infinity_polling()
