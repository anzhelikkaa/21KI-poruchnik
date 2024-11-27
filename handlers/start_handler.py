from telebot.types import ReplyKeyboardMarkup
from bot_instance import bot
from data.questions import questions
from data.user_data import user_data  

def show_topics(chat_id, user):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for topic in questions.keys():
        markup.add(topic)
    bot.send_message(
        chat_id,
        f"Вітаємо, {user.first_name}! Оберіть тему для початку вікторини.",
        reply_markup=markup
    )
