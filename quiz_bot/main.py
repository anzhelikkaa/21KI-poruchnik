from bot import bot
from handlers import register_handlers

def main():
    register_handlers(bot)
    bot.polling(none_stop=True)

if __name__ == '__main__':
    main()
