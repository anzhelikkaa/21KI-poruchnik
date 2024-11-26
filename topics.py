from telebot.types import ReplyKeyboardMarkup
from decorators import log_message


@log_message
def handle_topic_selection(message, bot):
    """Обробка вибору теми"""
    chat_id = message.chat.id
    selected_topic = message.text
    user_data[chat_id] = {'selected_topic': selected_topic}

    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add("Почати вікторину", "Повернутися до вибору теми")
    bot.send_message(chat_id, f"Ви вибрали тему: {selected_topic}. Бажаєте почати вікторину?", reply_markup=markup)
