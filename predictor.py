import random
import telebot
from telebot import types
import sqlite3
import datetime
from variables import token, frases, stickers, stick_for_badw, me, exx, you, mom, dad, serj, admin, putin, friend, \
    badwords, questions, boyfriend, girlfriend


def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['help'])
    def welcome_help(message):
        bot.send_message(message.chat.id,
                         "hmmm... I can't help you, but i can predict your future! And a little bit more. Tap on "
                         "/start for begin!")

    @bot.message_handler(commands=['start'])
    def start(message):
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Cats", url='https://genrandom.com/cats/')
        markup.add(button1)
        bot.send_message(message.chat.id, (
                "Hi, my soft kitty " + message.from_user.first_name + "! \nWrite me, about whom you wanna know the future? (^-^) \nOr you can enjoy  some cats. You know what to do with the button below.").format(
            message.from_user), reply_markup=markup)

    @bot.message_handler(content_types=["text"])
    def send_text(message):
        if message.text.lower() in me:
            bot.send_message(
                message.chat.id, random.choice(frases)
            )
            bot.send_sticker(message.chat.id, random.choice(stickers))
        elif message.text.lower() in you:
            bot.send_message(
                message.chat.id, (
                    "Not today, my sweety ( ́ ◕◞ε◟◕`) We're here to talk about you. Text me about yourself or somebody else.")
            )
        elif message.text.lower() in dad:
            bot.send_message(
                message.chat.id,
                ("Dad? Are you kidding? Ask me about your mom;) or somebody else, my sweety ( ́ ◕◞ε◟◕`)")
            )
        elif message.text.lower() in exx:
            bot.send_message(
                message.chat.id, ("Stop thinking about your ex. Your ex is a dumb. Let's eat ice cream ( ́ ◕◞ε◟◕`)")
            )
        elif message.text.lower() in boyfriend:
            bot.send_message(
                message.chat.id,
                ("Who are you kidding?, Text me about yourself, my sweety ( ́ ◕◞ε◟◕`)... P.S. Your bf a cutie")
            )
        elif message.text.lower() in admin:
            bot.send_message(
                message.chat.id, (
                    "Who are you kidding?, Text me about yourself, my sweety ( ́ ◕◞ε◟◕`)... P.S. Admin a cutie, like you <3")
            )
        elif message.text.lower() in girlfriend:
            bot.send_message(
                message.chat.id,
                ("Your girl is good, but you're the best, my sweety ( ́ ◕◞ε◟◕`)... Try to text about someone else")
            )
        elif message.text.lower() in mom:
            bot.send_sticker(message.chat.id,
                             "CAACAgIAAxkBAAEGhlljfliXgK4SgvYqvdUgwEOutJaF1gACAwADWcAHGR773jucAxpNKwQ")
            bot.send_message(
                message.chat.id,
                (
                    "Your mom is the best I ever know, my sweety ( ́ ◕◞ε◟◕`)... let's drink something together ;)")
            )
        elif message.text.lower() in serj:
            try:
                bot.send_message(
                    message.chat.id, ("You called the name of the emperor of kitties!")
                )
                bot.send_sticker(message.chat.id,
                                 "CAACAgIAAxkBAAEGgSFjfMLgFep9__PSKzgiUipVguhc7gAC0QADNuwbBQltUpd9jwABLCsE")
            except Exception as ex:
                print(ex)
        elif message.text.lower() in putin:
            try:
                bot.send_message(
                    message.chat.id, ("Nobody knows about him!")
                )
                bot.send_sticker(message.chat.id,
                                 "CAACAgIAAxkBAAEGgRhjfLs-CXviUI7gLv14_GzTaB3FqwACqQEAAjbsGwWX6dxaq6JjRisE")
            except Exception as ex:
                print(ex)
        elif message.text.lower() in badwords:
            try:
                bot.send_message(
                    message.chat.id, ("What did you say???")
                )
                bot.send_sticker(message.chat.id, random.choice(stick_for_badw))
            except Exception as ex:
                print(ex)
        elif message.text.lower() in questions:
            try:
                bot.send_sticker(message.chat.id,
                                 "CAACAgIAAxkBAAEGg_1jffHGGYDIk5b2XFiJep7BQ40zBgAC4QUAAjbsGwXqDYafNkGb_isE")
                bot.send_message(
                    message.chat.id, ("Dear " + message.from_user.first_name + ", I'm asking the questions here")
                )
            except Exception as ex:
                print(ex)
        else:
            bot.send_message(message.chat.id, "Ooops...Who is this?...(try to text 'Me' or someone else)")

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
