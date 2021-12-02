from typing import overload
import vk_api, vk
import json
import datetime
from vk_api import keyboard
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
from vk_api.longpoll import Event, VkLongPoll, VkEventType
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vkbot.bin.maindef import event_m_send, new_m_send

from vkbot.bin.settings import*
from vkbot.resources.timelessons import*
from vkbot.bin.keyboard import*
from vkbot.bin.maindef import event_m_send

rrasp = ''
rrtomorrow = ''

def day():

    day = datetime.datetime.today().weekday()

    global rrasp, rrtomorrow, overday

    day1 = 'Понедельник: \n\n 1. 8:30 - 9:10 Физика \n 2. 9:15 - 9:55 Физика \n 3. 10:05 - 10:45 Русский \n 4. 10:55 - 11:35 Математика \n 5. 11:40 - 12:20 Математика \n 6. 12:25 - 13:05 Английский \n 7. 13:10 - 13: 50 Физкультура \n 8. Физкультура\n\n\n'
    day2 = 'Вторник: \n\n 1. 8:30 - 9:10 Физика \n 2. 9:15 - 9:55 Литература \n 3. 10:05 - 10:45 Литература \n 4. 10:55 - 11:35 Русский \n 5. 11:40 - 12:20 Математика \n 6. 12:25 - 13:05 Математика \n 7. 13:10 - 13: 50 Инд.проект\n\n\n'
    day3 = 'Среда: \n\n 1. 8:30 - 9:10 История \n 2. 9:15 - 9:55 История \n 3. 10:05 - 10:45 Информатика \n 4. 10:55 - 11:35 Информатика \n 5. 11:40 - 12:20 Информатика\n'
    day4 = 'Четверг: \n\n 1. 8:30 - 9:10 Физика \n 2. 9:15 - 9:55 Физика \n 3. 10:05 - 10:45 Русский \n 4. 10:55 - 11:35 Литература \n 5. 11:40 - 12:20 Родная литература \n 6. 12:25 - 13:05 Математика \n 7. 13:10 - 13: 50 Математика\n\n\n'
    day5 = 'Пятница: \n\n 2. 8:30 - 9:10 Информатика \n 3. 9:15 - 9:55 Английский \n 4. 10:05 - 10:45 Английский \n 5. 11:40 - 12:20 Общество \n 6. 12:25 - 13:05 Общество \n 7. 13:10 - 13: 50 ОБЖ\n\n\n'
    overday = day1 + day2 + day3 + day4 + day5

    if day == 0:
        rrasp = day1
    elif day == 1:
        rrasp = day2
    elif day == 2:
        rrasp = day3
    elif day == 3:
        rrasp = day4
    elif day == 4:
        rrasp = day5
    else:
        rrasp = 'Сегодня уроков нет \n Расписание на понедельник: \n', day1

    if day == 0:
        rrtomorrow = day2
    elif day == 1:
        rrtomorrow = day3
    elif day == 2:
        rrtomorrow = day4
    elif day == 3:
        rrtomorrow = day5
    else:
        rrtomorrow = 'Сегодня уроков нет \n Расписание на понедельник: \n', day1




def rasp(event):
    last_id = vk_.messages.send(
                        user_id=event.object.user_id,
                        random_id=get_random_id(),
                        peer_id=event.object.peer_id,
                        keyboard = keyboard_6.get_keyboard(),
                        message = 'Расписание:'
                )
    day()

def r_today (event):
    global rrasp
    last_id = vk_.messages.send(
                        user_id=event.object.user_id,
                        random_id=get_random_id(),
                        peer_id=event.object.peer_id,
                        keyboard = keyboard_6.get_keyboard(),
                        message = rrasp
                )

def r_tomorrow (event):
    global rrtomorrow
    last_id = vk_.messages.send(
                        user_id=event.object.user_id,
                        random_id=get_random_id(),
                        peer_id=event.object.peer_id,
                        keyboard = keyboard_1.get_keyboard(),
                        message = rrtomorrow
                )

def r_poln (event):
    global overday
    last_id = vk_.messages.send(
                        user_id=event.object.user_id,
                        random_id=get_random_id(),
                        peer_id=event.object.peer_id,
                        keyboard = keyboard_1.get_keyboard(),
                        message = overday
                )
