# main.py

import telebot
from config import TOKEN
from handlers.start_handlers import register_start_handlers
from handlers.admin_handlers import register_admin_handlers

bot = telebot.TeleBot(TOKEN)

register_start_handlers(bot)
register_admin_handlers(bot)

print("Bot ishga tushdi ✅")
bot.infinity_polling()
