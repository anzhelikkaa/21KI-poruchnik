from datetime import datetime

def log_time(func):
    def wrapper(bot, chat_id):
        start_time = datetime.now()
        result = func(bot, chat_id)
        end_time = datetime.now()
        duration = end_time - start_time
        print(f"Вікторина завершена за {duration} секунд")
        return result
    return wrapper
