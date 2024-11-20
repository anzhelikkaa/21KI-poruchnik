import telebot
import random

bot = telebot.TeleBot('7898616545:AAFyxJ-cD0e8Uwk30RzK_dhJgLZYwmecG8U')

questions = {
'пиво': [
        {
            'question': 'Яка країна вважається батьківщиною пива?',
            'answers': ['Німеччина', 'Бельгія', 'Чехія'],
            'correct': 2
        },
        {
            'question': 'Який основний інгредієнт використовується для виготовлення пива?',
            'answers': ['Ячмінь', 'Вино', 'Сир'],
            'correct': 0
        },
        {
            'question': 'Як називається процес зброджування пива?',
            'answers': ['Вакцинація', 'Ферментація', 'Карбонізація'],
            'correct': 1
        },
        {
            'question': 'Який хімічний елемент визначає гіркоту пива?',
            'answers': ['Хлор', 'Калій', 'Хміль'],
            'correct': 2
        },
        {
            'question': 'Яке пиво відоме своєю міцною гіркотою і темним кольором?',
            'answers': ['Лагер', 'Стаут', 'Ель'],
            'correct': 1
        },
        {
            'question': 'Який алкогольний напій вважається «прадідом» пива?',
            'answers': ['Квас', 'Вино', 'Медовуха'],
            'correct': 2
        },
        {
            'question': 'В якому році було знайдено найстаріше написання рецепту пива?',
            'answers': ['3000 до н.е.', '1800 до н.е.', '1500 н.е.'],
            'correct': 0
        },
        {
            'question': 'Який місто вважається світовою столицею пива?',
            'answers': ['Дублін', 'Мюнхен', 'Брюссель'],
            'correct': 1
        },
        {
            'question': 'Який різновид пива зазвичай виготовляється в сезон осені?',
            'answers': ['Весняний Ель', 'Осінній Лагер', 'Октоберфестбір'],
            'correct': 2
        },
        {
            'question': 'Яка країна найбільший виробник пива у світі?',
            'answers': ['США', 'Китай', 'Німеччина'],
            'correct': 1
        },
        {
            'question': 'Який інгредієнт додається в пиво для додання ароматичних властивостей?',
            'answers': ['Ваніль', 'Хміль', 'Мед'],
            'correct': 1
        },
        {
            'question': 'Яка температура зазвичай використовується для зберігання пива?',
            'answers': ['0-5°C', '10-15°C', '20-25°C'],
            'correct': 0
        },
        {
            'question': 'Яка пивоварня вважається найстарішою діючою пивоварнею у світі?',
            'answers': ['Weihenstephan (Німеччина)', 'Guinness (Ірландія)', 'Budweiser (США)'],
            'correct': 0
        },
        {
            'question': 'Яке пиво найбільше відоме своєю фруктовою складовою?',
            'answers': ['IPA', 'Портер', 'Lambic'],
            'correct': 2
        },
        {
            'question': 'Яка країна є домом для найбільшої кількості різновидів пива?',
            'answers': ['Бельгія', 'Англія', 'Чехія'],
            'correct': 0
        }
    ],
    'музика': [
        {
            'question': 'Хто виконує пісню "Океан"?',
            'answers': ['Тіна Кароль', 'Океан Ельзи', 'Скрябін'],
            'correct': 1
        },
        {
            'question': 'Хто виконує пісню "Дикі танці"?',
            'answers': ['Руслана', 'NK (Настя Каменських)', 'Джамала'],
            'correct': 0
        },
        {
            'question': 'Хто виконує пісню "Вільний"?',
            'answers': ['СКАЙ', 'The Hardkiss', 'Без Обмежень'],
            'correct': 2
        },
        {
            'question': 'Хто виконує пісню "Стиль собачки"?',
            'answers': ['MOZGI', 'Потап і Настя', 'Время и Стекло'],
            'correct': 2
        },
        {
            'question': 'Хто виконує пісню "Я не здамся без бою"?',
            'answers': ['Океан Ельзи', 'Бумбокс', 'Скрябін'],
            'correct': 0
        },
        {
            'question': 'Хто виконує пісню "Тримай"?',
            'answers': ['Христина Соловій', 'Джамала', 'Тіна Кароль'],
            'correct': 0
        },
        {
            'question': 'Хто виконує пісню "Обійми"?',
            'answers': ['СКАЙ', 'Океан Ельзи', 'Бумбокс'],
            'correct': 1
        },
        {
            'question': 'Хто виконує пісню "На мосту"?',
            'answers': ['Антитіла', 'Каскадьори', 'O.Torvald'],
            'correct': 0
        },
        {
            'question': 'Хто виконує пісню "Стрілки"?',
            'answers': ['KAZKA', 'Время и Стекло', 'Джамала'],
            'correct': 0
        },
        {
            'question': 'Хто виконує пісню "Люди"?',
            'answers': ['Бумбокс', 'Океан Ельзи', 'The Hardkiss'],
            'correct': 2
        },
        {
            'question': 'Хто виконує пісню "Закрили твої очі"?',
            'answers': ['Тартак', 'Скрябін', 'Без Обмежень'],
            'correct': 2
        },
        {
            'question': 'Хто виконує пісню "Кожного дня"?',
            'answers': ['Бумбокс', 'Скрябін', 'СКАЙ'],
            'correct': 0
        },
        {
            'question': 'Хто виконує пісню "1944"?',
            'answers': ['Джамала', 'Тіна Кароль', 'Alyosha'],
            'correct': 0
        },
        {
            'question': 'Хто виконує пісню "До зустрічі"?',
            'answers': ['The Hardkiss', 'Kazka', 'Бумбокс'],
            'correct': 0
        },
        {
            'question': 'Хто виконує пісню "Злива"?',
            'answers': ['Джамала', 'Бумбокс', 'Скрябін'],
            'correct': 1
        }
    ],
    'географія': [
        {
            'question': 'Яка найбільша пустеля у світі?',
            'answers': ['Сахара', 'Гобі', 'Калахарі'],
            'correct': 0
        },
        {
            'question': 'Яка найдовша річка у світі?',
            'answers': ['Амазонка', 'Ніл', 'Янцзи'],
            'correct': 1
        },
        {
            'question': 'Яка найвища гора на Землі?',
            'answers': ['Кіліманджаро', 'Еверест', 'К2'],
            'correct': 1
        },
        {
            'question': 'Яке найбільше озеро за площею?',
            'answers': ['Вікторія', 'Суперіор', 'Каспійське море'],
            'correct': 2
        },
        {
            'question': 'Яка країна має найбільшу площу?',
            'answers': ['Канада', 'Китай', 'Росія'],
            'correct': 2
        },
        {
            'question': 'Яке місто є столицею Австралії?',
            'answers': ['Сідней', 'Мельбурн', 'Канберра'],
            'correct': 2
        },
        {
            'question': 'Яка країна найбільший за чисельністю населення?',
            'answers': ['Індія', 'Китай', 'США'],
            'correct': 1
        },
        {
            'question': 'Який океан є найглибшим?',
            'answers': ['Атлантичний', 'Індійський', 'Тихий'],
            'correct': 2
        },
        {
            'question': 'Яка держава є найбільшою острівною державою?',
            'answers': ['Гренландія', 'Австралія', 'Індонезія'],
            'correct': 2
        },
        {
            'question': 'Яка країна має найбільшу кількість озер?',
            'answers': ['Фінляндія', 'Канада', 'Росія'],
            'correct': 1
        },
        {
            'question': 'Яка найнижча точка на земній поверхні?',
            'answers': ['Долина Смерті', 'Маріанська западина', 'Мертве море'],
            'correct': 2
        },
        {
            'question': 'Яка найбільша країна в Африці за площею?',
            'answers': ['Алжир', 'Судан', 'Лівія'],
            'correct': 0
        },
        {
            'question': 'Яке місто є найзаселенішим у світі?',
            'answers': ['Нью-Йорк', 'Токіо', 'Шанхай'],
            'correct': 1
        },
        {
            'question': 'Яка країна має найбільшу лісистість?',
            'answers': ['Канада', 'Бразилія', 'Росія'],
            'correct': 2
        },
        {
            'question': 'Яке місто є столицею Канади?',
            'answers': ['Торонто', 'Оттава', 'Монреаль'],
            'correct': 1
        }
    ]
}

user_data = {}

def show_topics(chat_id, user):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for topic in questions.keys():
        markup.add(topic)
    bot.send_message(chat_id, f"Вітаємо, {user.first_name}! Раді вас бачити. Оберіть тему для початку вікторини.", reply_markup=markup)

def start_quiz(chat_id, topic):
    user_data[chat_id] = {'topic': topic, 'current_question': 0, 'score': 0, 'questions': random.sample(questions[topic], min(15, len(questions[topic])))}
    next_question(chat_id)

def next_question(chat_id):
    user = user_data[chat_id]
    current_question = user['current_question']
    question_data = user['questions'][current_question]

    # Створюємо клавіатуру з варіантами відповідей
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for answer in question_data['answers']:
        markup.add(answer)
    markup.add("Завершити")

    bot.send_message(chat_id, question_data['question'], reply_markup=markup)

def handle_quiz_decision(chat_id, decision, user):
    if decision == "Почати вікторину":
        selected_topic = user_data[chat_id]['selected_topic']
        start_quiz(chat_id, selected_topic)
    elif decision == "Повернутися до вибору теми":
        show_topics(chat_id, user)

@bot.message_handler(commands=['start'])
def handle_start(message):
    show_topics(message.chat.id, message.from_user)

@bot.message_handler(func=lambda message: message.text in questions.keys())
def handle_topic_selection(message):
    chat_id = message.chat.id
    selected_topic = message.text
    user_data[chat_id] = {'selected_topic': selected_topic}
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add("Почати вікторину", "Повернутися до вибору теми")
    bot.send_message(chat_id, f"Ви вибрали тему: {selected_topic}. Бажаєте почати вікторину?", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ["Почати вікторину", "Повернутися до вибору теми"])
def handle_quiz_decision_message(message):
    handle_quiz_decision(message.chat.id, message.text, message.from_user)

@bot.message_handler(func=lambda message: True)
def handle_answer(message):
    chat_id = message.chat.id
    user = user_data.get(chat_id)

    if not user:
        bot.send_message(chat_id, "Будь ласка, спочатку виберіть тему за допомогою команди /start.")
        return

    if message.text == "Завершити":
        calculate_results(chat_id)
        return
    elif message.text == "Повернутися до вибору теми":
        show_topics(chat_id, message.from_user)
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

def calculate_results(chat_id):
    user = user_data[chat_id]
    bot.send_message(chat_id, f"Вікторина завершена! Ваш результат: {user['score']} з {len(user['questions'])}.")
    del user_data[chat_id]
    bot.send_message(chat_id, "Бажаєте спробувати ще раз? Напишіть /start")

if __name__ == '__main__':
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"Сталася помилка: {e}")
