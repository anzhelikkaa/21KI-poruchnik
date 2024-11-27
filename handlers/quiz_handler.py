import telebot  # Додано імпорт telebot
from telebot.types import ReplyKeyboardMarkup
from bot_instance import bot
from data.questions import get_random_questions
from data.user_data import user_data

def start_quiz(chat_id, topic):
    user_data[chat_id] = {
        'topic': topic,
        'current_question': 0,
        'score': 0,
        'questions': get_random_questions(topic)
    }
    next_question(chat_id)

def next_question(chat_id):
    user = user_data[chat_id]
    question_data = user['questions'][user['current_question']]

    # Створюємо клавіатуру
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for answer in question_data['answers']:
        markup.add(answer)
    markup.add("Завершити")

    bot.send_message(chat_id, question_data['question'], reply_markup=markup)

def handle_answer(chat_id, text):
    user = user_data[chat_id]
    if text == "Завершити":
        calculate_results(chat_id)
        return

    current_question = user['current_question']
    question_data = user['questions'][current_question]

    if text == question_data['answers'][question_data['correct']]:
        user['score'] += 1
        bot.send_message(chat_id, "Правильно!")
    else:
        bot.send_message(chat_id, f"Неправильно. Правильна відповідь: {question_data['answers'][question_data['correct']]}")

    user['current_question'] += 1
    if user['current_question'] < len(user['questions']):
        next_question(chat_id)
    else:
        calculate_results(chat_id)

def calculate_results(chat_id):
    user = user_data[chat_id]
    bot.send_message(chat_id, f"Вікторина завершена! Ваш результат: {user['score']} з {len(user['questions'])}.")
    del user_data[chat_id]
    bot.send_message(chat_id, "Бажаєте спробувати ще раз? Напишіть /start")