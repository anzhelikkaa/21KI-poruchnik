from telebot.types import ReplyKeyboardMarkup
from decorators import log_message

@log_message
def handle_start(message, bot):
    """Обробка команди /start"""
    chat_id = message.chat.id
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for topic in questions.keys():
        markup.add(topic)
    bot.send_message(chat_id, f"Вітаємо, {message.from_user.first_name}! Оберіть тему для початку вікторини.", reply_markup=markup)
