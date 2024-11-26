from telebot import *
from bot_config import *
from questions import *
from start import *
from topics import *
from quiz import *

bot = TeleBot(BOT_TOKEN)

# Реєстрація хендлерів
bot.message_handler(commands=['start'])(handle_start)
bot.message_handler(func=lambda message: message.text in questions.keys())(handle_topic_selection)
bot.message_handler(func=lambda message: message.text in ["Почати вікторину", "Повернутися до вибору теми"])(handle_quiz_decision_message)
bot.message_handler(func=lambda message: True)(handle_answer)

if __name__ == "__main__":
    bot.polling(none_stop=True)
