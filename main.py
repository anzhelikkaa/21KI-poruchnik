from bot_instance import bot
from handlers.start_handler import show_topics
from handlers.topic_handler import handle_topic_selection
from handlers.quiz_handler import start_quiz, handle_answer
from data.questions import questions
from data.user_data import user_data  # Імпортуємо user_data із data.user_data

@bot.message_handler(commands=['start'])
def handle_start(message):
    show_topics(message.chat.id, message.from_user)

@bot.message_handler(func=lambda message: message.text in questions.keys())
def topic_selection(message):
    handle_topic_selection(message.chat.id, message.text)

@bot.message_handler(func=lambda message: message.text in ["Почати вікторину", "Повернутися до вибору теми"])
def quiz_decision(message):
    chat_id = message.chat.id
    if message.text == "Почати вікторину":
        topic = user_data[chat_id]['selected_topic']
        start_quiz(chat_id, topic)
    elif message.text == "Повернутися до вибору теми":
        show_topics(chat_id, message.from_user)

@bot.message_handler(func=lambda message: True)
def answer_handler(message):
    handle_answer(message.chat.id, message.text)

if __name__ == '__main__':
    bot.polling(none_stop=True)