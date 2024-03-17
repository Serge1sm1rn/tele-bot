
import telebot
from telebot import types
import webbrowser

bot = telebot.TeleBot('6339530193:AAHeidjwl7SZ9wY19KoYv_pb5K5z_6dgObs')


@bot.message_handler(commands=['start'])
def get_photo(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton(
        text='Открыть сайт')
    markup.row(btn1)
    btn2 = types.KeyboardButton(
        text='Удалить фото')
    btn3 = types.KeyboardButton(
        text='Изменить текст')
    markup.row(btn2, btn3)
    bot.reply_to(
        message,
        text=f'Привет, {message.from_user.first_name} {message.from_user.last_name}!',
        reply_markup=markup)
    bot.register_next_step_handler(message, on_click)


def on_click(message):
    if message.text == 'Открыть сайт':
        webbrowser.open('https://github.com/Serge1sm1rn/tele-bot')
    elif message.text == 'Удалить фото':
        bot.delete_message(
            message.chat.id,
            message.message_id - 1)
    elif message.text == 'Изменить текст':
        bot.edit_message_text(
            'Edited text',
            message.chat.id,
            message.message_id)


@bot.message_handler(commands=['site', 'website',])
def site(message):
    webbrowser.open('https://github.com/Serge1sm1rn/tele-bot')
    bot.send_message(message.chat.id, 'Сайт открыт!')


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(
        text='Открыть сайт',
        url='https://github.com/Serge1sm1rn/tele-bot')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton(
        text='Удалить фото',
        callback_data='delete_photo')
    btn3 = types.InlineKeyboardButton(
        text='Изменить текст',
        callback_data='edit_text')
    markup.row(btn2, btn3)
    bot.reply_to(message, text='Выберите фото', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete_photo':
        bot.delete_message(
            callback.message.chat.id,
            callback.message.message_id - 1)
    elif callback.data == 'edit_text':
        bot.edit_message_text(
            'Edited text',
            callback.message.chat.id,
            callback.message.message_id)


bot.infinity_polling()
