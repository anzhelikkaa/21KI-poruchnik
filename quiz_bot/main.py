import telebot
from quiz_utils import *

# Ініціалізація бота
TELEGRAM_BOT_TOKEN = get_token()
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

def main():
    @bot.message_handler(commands=['start'])
    def handle_start(message):
        chat_id = message.chat.id
        user = message.from_user
        markup = create_topic_markup()
        bot.send_message(chat_id, f"Вітаємо, {user.first_name}! Оберіть тему для вікторини.", reply_markup=markup)

    @bot.message_handler(func=lambda message: message.text in randomize_questions().keys())
    def handle_topic_selection(message):
        chat_id = message.chat.id
        user_data[chat_id] = {'selected_topic': message.text}
        markup = create_decision_markup()
        bot.send_message(chat_id, f"Ви вибрали тему: {message.text}. Бажаєте почати вікторину?", reply_markup=markup)

    @bot.message_handler(func=lambda message: message.text in ["Почати вікторину", "Повернутися до вибору теми"])
    def handle_decision(message):
        chat_id = message.chat.id
        if message.text == "Почати вікторину":
            start_quiz(chat_id)
        elif message.text == "Повернутися до вибору теми":
            markup = create_topic_markup()
            bot.send_message(chat_id, "Оберіть тему:", reply_markup=markup)
    @log_time
    def start_quiz(chat_id):
        topic = user_data[chat_id]['selected_topic']
        user_data[chat_id].update({
            'topic': topic,
            'current_question': 0,
            'score': 0,
            'questions': randomize_questions()[topic],
        })
        next_question(chat_id)

    def next_question(chat_id):
        user = user_data[chat_id]
        question_data = user['questions'][user['current_question']]
        markup = create_answer_markup(question_data['answers'])
        bot.send_message(chat_id, question_data['question'], reply_markup=markup)

    @bot.message_handler(func=lambda message: True)
    def handle_answer(message):
        chat_id = message.chat.id
        user = user_data.get(chat_id)

        if not user:
            bot.send_message(chat_id, "Спочатку виберіть тему за допомогою команди /start.")
            return

        if message.text == "Завершити":
            calculate_results(chat_id)
            return

        current_question = user['current_question']
        question_data = user['questions'][current_question]

        if message.text == question_data['answers'][question_data['correct']]:
            user['score'] += 1
            bot.send_message(chat_id, "Правильно!")
        else:
            correct_answer = question_data['answers'][question_data['correct']]
            bot.send_message(chat_id, f"Неправильно. Правильна відповідь: {correct_answer}")

        user['current_question'] += 1
        if user['current_question'] < len(user['questions']):
            next_question(chat_id)
        else:
            calculate_results(chat_id)

    @log_time
    def calculate_results(chat_id):
        user = user_data[chat_id]
        bot.send_message(chat_id, f"Вікторина завершена! Ваш результат: {user['score']} з {len(user['questions'])}.")
        del user_data[chat_id]
        bot.send_message(chat_id, "Бажаєте спробувати ще раз? Напишіть /start")

    bot.infinity_polling()

if __name__ == '__main__':
    main()
