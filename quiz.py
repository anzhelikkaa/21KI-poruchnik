import random
from telebot.types import ReplyKeyboardMarkup
from decorators import log_message

user_data = {}


@log_message
def handle_quiz_decision_message(message, bot):
    """Обробка рішень у вікторині"""
    chat_id = message.chat.id
    decision = message.text

    if decision == "Почати вікторину":
        selected_topic = user_data[chat_id]['selected_topic']
        start_quiz(chat_id, selected_topic, bot)
    elif decision == "Повернутися до вибору теми":
        show_topics(chat_id, message.from_user, bot)


def start_quiz(chat_id, topic, bot):
    """Початок вікторини"""
    user_data[chat_id] = {
        'topic': topic,
        'current_question': 0,
        'score': 0,
        'questions': random.sample(questions[topic], min(15, len(questions[topic])))
    }
    next_question(chat_id, bot)


def next_question(chat_id, bot):
    """Показ наступного питання"""
    user = user_data[chat_id]
    current_question = user['current_question']
    question_data = user['questions'][current_question]

    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for answer in question_data['answers']:
        markup.add(answer)
    markup.add("Завершити")

    bot.send_message(chat_id, question_data['question'], reply_markup=markup)


@log_message
def handle_answer(message, bot):
    """Обробка відповідей користувача"""
    chat_id = message.chat.id
    user = user_data.get(chat_id)

    if not user:
        bot.send_message(chat_id, "Будь ласка, спочатку виберіть тему за допомогою команди /start.")
        return

    if message.text == "Завершити":
        calculate_results(chat_id, bot)
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
        next_question(chat_id, bot)
    else:
        calculate_results(chat_id, bot)


def calculate_results(chat_id, bot):
    """Підрахунок результатів"""
    user = user_data[chat_id]
    bot.send_message(chat_id, f"Вікторина завершена! Ваш результат: {user['score']} з {len(user['questions'])}.")
    del user_data[chat_id]
    bot.send_message(chat_id, "Бажаєте спробувати ще раз? Напишіть /start")
