
import telebot

bot = telebot.TeleBot('6339530193:AAHeidjwl7SZ9wY19KoYv_pb5K5z_6dgObs')


@bot.message_handler(commands=['start', 'help', 'hello'])
def main(message):

    bot.send_message(
        message.chat.id,
        f'Привет, {message.from_user.first_name} {message.from_user.last_name}!')


@bot.message_handler(content_types=['text'])
def main(message):
    bot.send_message(message.chat.id, message.text)


@bot.message_handler(commands=['start'])
def main(message):

    bot.send_message(message.chat.id, 'Привет!')


bot.infinity_polling()
