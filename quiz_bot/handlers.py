import telebot
from quiz import show_topics, handle_quiz_decision, handle_answer, handle_topic_selection

def register_handlers(bot):
    @bot.message_handler(commands=['start'])
    def handle_start(message):
        show_topics(bot, message.chat.id, message.from_user)

    @bot.message_handler(func=lambda message: message.text in ["Почати вікторину", "Повернутися до вибору теми"])
    def handle_quiz_decision_message(message):
        handle_quiz_decision(bot, message.chat.id, message.text, message.from_user)

    @bot.message_handler(func=lambda message: message.text in ['пиво', 'музика', 'географія'])
    def handle_topic(message):
        handle_topic_selection(bot, message.chat.id, message.text)

    @bot.message_handler(func=lambda message: True)
    def handle_all_messages(message):
        handle_answer(bot, message)
