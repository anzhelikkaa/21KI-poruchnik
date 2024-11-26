import logging

def log_message(func):
    def wrapper(*args, **kwargs):
        message = args[0]
        logging.info(f"Handling message: {message.text}")
        return func(*args, **kwargs)
    return wrapper
