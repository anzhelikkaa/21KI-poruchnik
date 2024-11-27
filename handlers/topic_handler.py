from telebot.types import ReplyKeyboardMarkup
from bot_instance import bot
from data.user_data import user_data

def handle_topic_selection(chat_id, selected_topic):
    user_data[chat_id] = {'selected_topic': selected_topic}
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add("Почати вікторину", "Повернутися до вибору теми")
    bot.send_message(chat_id, f"Ви вибрали тему: {selected_topic}. Бажаєте почати вікторину?", reply_markup=markup)
