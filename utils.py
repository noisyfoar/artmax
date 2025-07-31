import os
from dotenv import load_dotenv
import telebot

load_dotenv()

URLS = os.getenv("BRANCH_URLS", "").split(",")
token = os.getenv("TG_BOT_TOKEN")
chat_id = os.getenv("TG_CHAT_ID")
bot = telebot.TeleBot(token)


async def send_notification(url, count):
    text = f"В филиал: {url} \n добавлено {count} отзывов"
    bot.send_message(chat_id, text)
    
