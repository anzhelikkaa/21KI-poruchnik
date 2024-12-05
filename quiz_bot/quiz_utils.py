import os
import random
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv
from datetime import datetime

# Завантаження токена бота
def get_token():
    load_dotenv()
    return os.getenv('TELEGRAM_BOT_TOKEN')

# Питання для вікторини
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

def randomize_questions():
    return {topic: random.sample(data, min(15, len(data))) for topic, data in questions.items()}

# Створення клавіатур
def create_topic_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for topic in questions.keys():
        markup.add(KeyboardButton(topic))
    return markup

def create_decision_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(KeyboardButton("Почати вікторину"), KeyboardButton("Повернутися до вибору теми"))
    return markup

def create_answer_markup(answers):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for answer in answers:
        markup.add(KeyboardButton(answer))
    markup.add(KeyboardButton("Завершити"))
    return markup

# Декоратор для логування часу
def log_time(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.now()
        duration = end_time - start_time
        print(f"Функція {func.__name__} завершена за {duration} секунд")
        return result
    return wrapper

