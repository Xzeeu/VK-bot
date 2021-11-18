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

day = datetime.datetime.today().weekday()

rrasp = ''
rrtomorrow = ''

day1 = 'Понедельник: \n\n 1. Физика \n 2. Физика \n 3. Русский \n 4. Математика \n 5. Математика \n 6. Английский \n 7. Физкультура \n 8. Физкультура\n\n\n'
day2 = 'Вторник: \n\n 1. Физика \n 2. Литература \n 3. Литература \n 4. Русский \n 5. Математика \n 6. Математика \n 7. Инд.проект\n\n\n'
day3 = 'Среда: \n\n 1. История \n 2. История \n 3. Информатика \n 4. Информатика \n 5. Информатика\n'
day4 = 'Четверг: \n\n 1. Физика \n 2. Физика \n 3. Русский \n 4. Литература \n 5. Родная литература \n 6. Математика \n 7. Математика\n\n\n'
day5 = 'Пятница: \n\n 2. Информатика \n 3. Английский \n 4. Английский \n 5. Общество \n 6. Общество \n 7. ОБЖ\n\n\n'
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

def r_today (event):
    last_id = vk_.messages.send(
                        user_id=event.object.user_id,
                        random_id=get_random_id(),
                        peer_id=event.object.peer_id,
                        keyboard = keyboard_6.get_keyboard(),
                        message = rrasp
                )

def r_tomorrow (event):
    last_id = vk_.messages.send(
                        user_id=event.object.user_id,
                        random_id=get_random_id(),
                        peer_id=event.object.peer_id,
                        keyboard = keyboard_1.get_keyboard(),
                        message = rrtomorrow
                )

def r_poln (event):
    last_id = vk_.messages.send(
                        user_id=event.object.user_id,
                        random_id=get_random_id(),
                        peer_id=event.object.peer_id,
                        keyboard = keyboard_1.get_keyboard(),
                        message = overday
                )
