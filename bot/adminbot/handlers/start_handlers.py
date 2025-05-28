# handlers/start_handlers.py

from telebot import TeleBot
from utils.user_manager import save_user

def register_start_handlers(bot: TeleBot):

    @bot.message_handler(commands=['start'])
    def start_handler(message):
        save_user(message.from_user.id)
        bot.send_message(message.chat.id, "Assalomu alaykum! Botga xush kelibsiz 🤖")
