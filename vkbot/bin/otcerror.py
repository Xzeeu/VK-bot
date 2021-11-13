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
from vkbot.resources.timelessons import*
from vkbot.bin.keyboard import*
#from vkbot.bin.otcerror import o_error
from vkbot.bin.timetable import tt
from vkbot.bin.maindef import *

error = False
DZ = False
error_el = 'g'
DZ_el = ''

def o_error(event):

    global error, error_el

    if event.obj.message['text'] == 'Секреты':
            if error_el != '':
                if event.from_user:
                    new_m_send(event, keyboard_4.get_keyboard(), error_el)
                    
            else:
                if event.from_user:
                    new_m_send(event, None, 'Сообщений об ошибках нет.')
    return

def ro_error(event):
    
    global error, error_el

    event_m_send(event, None, 'Пожалуйста, опишите ошибку в следующем сообщении.')
    error = True

def roo_error(event):
    global error, error_el

    if error == True:
        if event.obj.message != None:
            error_el += (str(event.obj.message) + '\n')
            error = False
    
    return error_el, error

def del_error(event):
    global error_el
    error_el = ''