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
from vkbot.bin.maindef import last_m_send

from vkbot.bin.settings import*
from vkbot.bin.keyboard import*

settings_2 = dict(one_time=False, inline=True)

keyboard_10 = VkKeyboard(**settings_2)

keyboard_10.add_callback_button(label='Ухаживать за животными', color=VkKeyboardColor.POSITIVE, payload={"type": "01"})
keyboard_10.add_line()
keyboard_10.add_callback_button(label='Обслуживать машины, приборы', color=VkKeyboardColor.POSITIVE, payload={"type": "10"})

keyboard_11 = VkKeyboard(**settings_2)

keyboard_11.add_callback_button(label='Узнать результат', color=VkKeyboardColor.POSITIVE, payload={"type": "rez"})

f_toggle: bool = False

a = 0
b = 0

def proftest(event):
    
    last_id = vk_.messages.send(
                        user_id=event.object.user_id,
                        random_id=get_random_id(),
                        peer_id=event.object.peer_id,
                        keyboard = keyboard_1.get_keyboard(),
                        message = 'Пройди тест!!!!!!!!!!!!!!!!!!!!!!!!!!1'
                )
                
    last_id = vk_.messages.send(
                        user_id=event.object.user_id,
                        random_id=get_random_id(),
                        peer_id=event.object.peer_id,
                        keyboard = keyboard_10.get_keyboard(),
                        message = 'Какую работу вы предпочтёте?'
                )




def aproftest(event):
    global a, b
    if event.type == VkBotEventType.MESSAGE_EVENT:
        if event.object.payload.get('type') == '01':
            a += 1
            rezultat(event)
        if event.object.payload.get('type') == '10':
            b += 1
            rezultat(event)



def rezultat(event):
    global a, b
    if a > 0:
        last_id = vk_.messages.send(
                            user_id=event.object.user_id,
                            random_id=get_random_id(),
                            peer_id=event.object.peer_id,
                            message = 'Тест пройден!'
                    )
        last_id = vk_.messages.send(
                            user_id=event.object.user_id,
                            random_id=get_random_id(),
                            peer_id=event.object.peer_id,
                            message = 'Поступай на доярку в Курганскую государственную сельскохозяйственную академию им. Т. С. Мальцева \n на специальность Зоотехния \n сайт: http://www.ksaa.zaural.ru/'
                    )
        a = 0
    if b > 0:
        last_id = vk_.messages.send(
                            user_id=event.object.user_id,
                            random_id=get_random_id(),
                            peer_id=event.object.peer_id,
                            message = 'Тест пройден!'
                    )
        last_id = vk_.messages.send(
                            user_id=event.object.user_id,
                            random_id=get_random_id(),
                            peer_id=event.object.peer_id,
                            message = 'Поступай на автосервисника в Курганский государственный университет \n на специальность Автомобильное хозяйство и автосервис \n сайт: http://www.kgsu.ru/ '
                    )
        b = 0