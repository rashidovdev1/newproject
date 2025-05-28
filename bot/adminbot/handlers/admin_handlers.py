# handlers/admin_handlers.py

from telebot import TeleBot
from config import ADMIN_ID
from utils.user_manager import load_users

def register_admin_handlers(bot: TeleBot):

    @bot.message_handler(commands=['broadcast'])
    def broadcast_handler(message):
        if message.from_user.id != ADMIN_ID:
            return

        msg = bot.send_message(message.chat.id, "Yubormoqchi bo'lgan xabaringizni yuboring (matn/raskm/video/audio):")
        bot.register_next_step_handler(msg, send_broadcast)

    def send_broadcast(message):
        users = load_users()

        for user_id in users:
            try:
                if message.content_type == 'text':
                    bot.send_message(user_id, message.text)
                elif message.content_type == 'photo':
                    bot.send_photo(user_id, message.photo[-1].file_id, caption=message.caption)
                elif message.content_type == 'video':
                    bot.send_video(user_id, message.video.file_id, caption=message.caption)
                elif message.content_type == 'audio':
                    bot.send_audio(user_id, message.audio.file_id, caption=message.caption)
                else:
                    bot.send_message(user_id, "Bot orqali bu formatni yuborib bo'lmaydi.")
            except Exception as e:
                print(f"Xabar yuborilmadi {user_id}: {e}")

        bot.send_message(ADMIN_ID, "✅ Xabar barcha foydalanuvchilarga yuborildi.")

    @bot.message_handler(commands=['users'])
    def users_list_handler(message):
        if message.from_user.id != ADMIN_ID:
            return
        users = load_users()
        bot.send_message(message.chat.id, f"Bot foydalanuvchilari soni: {len(users)} ta")
