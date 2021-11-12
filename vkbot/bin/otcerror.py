import vk_api, vk
import json
from datetime import datetime
from vk_api import keyboard
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

from vkbot.bin.settings import*
from vkbot.du.timelessons import*
from vkbot.bin.keyboard import*

error = False
DZ = False
error_el = ''
DZ_el = ''


def o_error(event):
    if error_el != '':
                if event.from_user:
                    vk_.messages.send(
                            user_id=event.obj.message['from_id'],
                            random_id=get_random_id(),
                            peer_id=event.obj.message['from_id'],
                            keyboard=keyboard_4.get_keyboard(),
                            message= error_el
                    )
    else:
        if event.from_user:
                        vk_.messages.send(
                                user_id=event.obj.message['from_id'],
                                random_id=get_random_id(),
                                peer_id=event.obj.message['from_id'],
                                message= 'Сообщений об ошибках нет.'
                        )
        return