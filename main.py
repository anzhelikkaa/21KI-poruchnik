import telebot
from config import *



bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def message_handler(message):
    bot.send_message(message.chat.id, message.text)



if __name__ == '__main__':
    bot.polling(True)