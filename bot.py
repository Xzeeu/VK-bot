import vk_api, vk
import json
from datetime import datetime
from vk_api import keyboard
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vkbot.bin.otcerror import del_error, o_error, ro_error, roo_error

from vkbot.bin.settings import*
from vkbot.resources.timelessons import*
from vkbot.bin.keyboard import*
#from vkbot.bin.otcerror import o_error
from vkbot.bin.timetable import tt
from vkbot.bin.maindef import *

#error = False
DZ = False
#error_el = ''
DZ_el = ''


for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        roo_error(event)

        if event.obj.message['text'] == 'Начать':
            if event.from_user:
                if 'callback' not in event.obj.client_info['button_actions']:
                    print(f'Клиент {event.obj.message["from_id"]} не поддерж. callback')
        
                new_m_send(event, keyboard_1.get_keyboard(), 'Привет')

        if event.obj.message['text'] == 'Секреты':
            o_error(event)
        

            '''if error_el != '':
                if event.from_user:
                    new_m_send(event, keyboard_4.get_keyboard(), error_el)
                    
            else:
                if event.from_user:
                    new_m_send(event, None, 'Сообщений об ошибках нет.')'''


    '''if error == True:
        if event.obj.message != None:
            error_el += (str(event.obj.message) + '\n')
            error = False'''
    if DZ == True:
        if event.obj.message != None:
            event.obj.message = event.obj.message['text']
            DZ_el += (str(event.obj.message) + '\n')
            DZ = False


    

    elif event.type == VkBotEventType.MESSAGE_EVENT:
        if event.object.payload.get('type') in CALLBACK_TYPES:
            r = vk_.messages.sendMessageEventAnswer(
                      event_id=event.object.event_id,
                      user_id=event.object.user_id,
                      peer_id=event.object.peer_id,                                                   
                      event_data=json.dumps(event.object.payload))
        #o_error(event)
        elif event.object.payload.get('type') == 'error':
            ro_error(event)
        
            '''event_m_send(event, None, 'Пожалуйста, опишите ошибку в следующем сообщении.')
            error = True'''

        elif event.object.payload.get('type') == 'error_del':
            del_error(event)

        if event.object.payload.get('type') == 'DZ_del':
            DZ_el = ''

        elif event.object.payload.get('type') == 'dz':
            if DZ_el == '':
                event_m_send(event, keyboard_3.get_keyboard(), 'Домашнее задание')

            if DZ_el != '':
                event_m_send(event, keyboard_5.get_keyboard(), DZ_el)


        elif event.object.payload.get('type') == '+dz':
            event_m_send(event, None, 'Пиши ДЗ.')

            DZ = True
            

        elif event.object.payload.get('type') == 'callback':
            tt(event)


if __name__ == '__main__':
    print()