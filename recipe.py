import random
import telebot
from telebot import types
import sqlite3
import datetime
from var import token, recipe, food


def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['help'])
    def welcome_help(message):
        bot.send_message(message.chat.id,
                         "С этим я не помогу, а вот пару рецептов пришлю. Нажми на "
                         "/start чтобы начать!")

    @bot.message_handler(commands=['start'])
    def start(message):
        # markup = types.InlineKeyboardMarkup()
        # button1 = types.InlineKeyboardButton("*********", url='***************')
        # markup.add(button1)
        bot.send_sticker(message.chat.id, "CAACAgQAAxkBAAEGtMdjjyIQd1sjeFG3BzFTGIZ8cOBAmAACJwAD8mXUBogfq2AeX3VJKwQ")
        bot.send_message(message.chat.id, (
                "Привет, хозяюшка " + message.from_user.first_name + "!\nЧто будем готовить? Обед? Ужин?").format(
            message.from_user))

    @bot.message_handler(content_types=["text"])
    def send_text(message):
        if message.text.lower() in food:
            bot.send_message(
                message.chat.id, random.choice(recipe)
            )
            bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEGtMljjyOi_Ink1QSfl7gH5lUREH_G-wACrwAD_E_gFYmj6yhkmYz0KwQ")
        else:
            bot.send_sticker(message.chat.id, "CAACAgQAAxkBAAEGtQ9jjz7mKXDSzHjJR7tUP2ub_3AoBAACDgAD8mXUBorYbrrXxzVOKwQ")
            bot.send_message(message.chat.id, "Это ещё что такое??? Напиши мне 'обед или ужин'.")

        def db_table_val(user_id: int, user_name: str, user_surname: str, username: str, visit_time: datetime):
            cursor.execute(
                'INSERT INTO test (user_id, user_name, user_surname, username, visit_time) VALUES (?, ?, ?, ?, ?)',
                (user_id, user_name, user_surname, username, visit_time))
            conn.commit()

        conn = sqlite3.connect('db/dbdt.db', check_same_thread=False, detect_types=sqlite3.PARSE_DECLTYPES |
                                                                                   sqlite3.PARSE_COLNAMES)
        cursor = conn.cursor()
        currentDateTime = datetime.datetime.now()
        us_id = message.from_user.id
        us_name = message.from_user.first_name
        us_sname = message.from_user.last_name
        username = message.from_user.username
        v_time = currentDateTime
        db_table_val(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username,
                     visit_time=v_time)

    bot.polling(none_stop=True)


if __name__ == '__main__':
    # get_data()
    telegram_bot(token)
