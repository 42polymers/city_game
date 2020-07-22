import telebot

from telebot import types
from random import choice
from random import shuffle

import django
django.setup()

from src.telegram.localization import *
from src.telegram.settings import bot_id
from src.web_client.system.models import Team, User

bot = telebot.TeleBot(bot_id)

NICKNAME = ''
PASSWORD = ''


@bot.message_handler(content_types=['text'])
def start(message):
    try:
        user = User.objects.get(id=message.from_user.id)
    except User.DoesNotExist:
        return authorization(message)
    if user.role == User.ADMIN:
        god_mode(message)
    else:
        keyboard = types.InlineKeyboardMarkup()
        key_answer = types.InlineKeyboardButton(text='Ввести ответ', callback_data='answer')
        key_help = types.InlineKeyboardButton(text='Подсказка', callback_data='help')
        key_rules = types.InlineKeyboardButton(text='Правила', callback_data='rules')
        key_status = types.InlineKeyboardButton(text='Статус', callback_data='status')
        keyboard.add(key_help, key_rules, key_status, key_answer)
        team_obj = user.team
        try:
            [0][1]
            # current_task = task_collection.find_one(
            #     {'_id': team_obj["tasks_ids"][team_obj["task_point"]]})
        except IndexError:
            bot.send_message(message.from_user.id, text="Ты либо решил все загадки, либо выпал "
                                                        "'index out of range'. В любом случае - поздравляю)")
            return
        try:
            img = open(f'media/tasks/{team_obj["tasks_ids"][team_obj["task_point"]]}.jpg', 'rb')
        except FileNotFoundError:
            img = open(f'media/oops.jpg', 'rb')
        bot.send_message(message.from_user.id, text=current_task["text"])

        bot.send_photo(message.from_user.id, img, reply_markup=keyboard)


def authorization(message):
    bot.send_message(message.from_user.id, 'Назовись, избранный!')
    bot.register_next_step_handler(message, get_password)


def get_password(message):
    bot.send_message(message.from_user.id, 'Каков твой пароль?')
    name = message.text
    bot.register_next_step_handler(message, get_destiny, name=name)


def get_destiny(message, name=None):

    try:
        team = Team.objects.get(token=message.text)
    except Team.DoesNotExist:
        return bot.send_message(message.from_user.id, TOKEN_FAIL)

    User.objects.create(**{'user_id': message.from_user.id,
                           'username': message.from_user.username,
                           'role': 'player',
                           'team_id': team.id})
    bot.send_message(message.from_user.id, TOKEN_SUCCESS)


def get_menu_text(team_obj):
    return f'Ты гордый представитель команды №{team_obj["_id"]}. Вы находитесь на ' \
        f'контрольной точке №{team_obj["task_point"] + 1},' \
        f' у вашей команды {team_obj["team_points"]} очков'


def god_mode(message):
    pass


bot.polling(none_stop=True, interval=0)
