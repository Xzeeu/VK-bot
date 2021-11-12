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
from vkbot.bin.otcerror import o_error

error = False
DZ = False
error_el = ''
DZ_el = ''

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        
        if event.obj.message['text'] == 'Начать':
            if event.from_user:
                if 'callback' not in event.obj.client_info['button_actions']:
                    print(f'Клиент {event.obj.message["from_id"]} не поддерж. callback')
        
                vk_.messages.send(
                        user_id=event.obj.message['from_id'],
                        random_id=get_random_id(),
                        peer_id=event.obj.message['from_id'],
                        keyboard=keyboard_1.get_keyboard(),
                        message= 'Привет!😊)'
                )

        if event.obj.message['text'] == 'Секреты':
            o_error(event)

    if error == True:
        if event.obj.message != None:
            error_el += (str(event.obj.message) + '\n')
            error = False
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

        elif event.object.payload.get('type') == 'error':
            last_id = vk_.messages.send(
                        user_id=event.object.user_id,
                        random_id=get_random_id(),
                        peer_id=event.object.peer_id,
                        message= 'Пожалуйста, опишите ошибку в следующем сообщении.'
                )
            error = True

        elif event.object.payload.get('type') == 'error_del':
            error_el = ''
        elif event.object.payload.get('type') == 'DZ_del':
            DZ_el = ''

        elif event.object.payload.get('type') == 'dz':
            if DZ_el == '':
                last_id = vk_.messages.send(
                            user_id=event.object.user_id,
                            random_id=get_random_id(),
                            peer_id=event.object.peer_id,
                            message= 'Домашнее задание',
                            keyboard=keyboard_3.get_keyboard()
                    )
            if DZ_el != '':
                last_id = vk_.messages.send(
                            user_id=event.object.user_id,
                            random_id=get_random_id(),
                            peer_id=event.object.peer_id,
                            message= DZ_el,
                            keyboard=keyboard_5.get_keyboard()
                    )

        elif event.object.payload.get('type') == '+dz':
            last_id = vk_.messages.send(
                        user_id=event.object.user_id,
                        random_id=get_random_id(),
                        peer_id=event.object.peer_id,
                        message= 'Пиши ДЗ.'
                )
            DZ = True
            


        elif event.object.payload.get('type') == 'callback':

            now  = datetime.now()

            k = 0


            H = 0
            M = 0

            a = str(now)
            a = a.split(' ')
            a = a[1]
            a2 = int(a[0:2]) + 5
            a1 = int(a[3:5])

            if a2 == 8:
                    H = h1
                    M = m1
                    k = 1
            if a2 == 9:
                    if a1 < 10:
                        H = h1
                        M = m1
                        k = 1
                    if a1 > 10:
                        H = h2
                        M = m2
                        k = 2
            if a2 == 10:
                    if a1 > 55:
                        H = h4
                        M = m4
                        k = 4
                    else:
                        H = h3
                        M = m3
                        k = 3
            if a2 == 11:
                    if a1 < 35:
                        H = h4
                        M = m4
                        k = 4
                    else:
                        H = h5
                        M = m5
                        k = 5
            if a2 == 12:
                    if a1 < 20:
                        H = h5
                        M = m5
                        k = 5
                    else:
                        H = h6
                        M = m6
                        k = 6
            if a2 == 13:
                    if a1 < 5:
                        H = h6
                        M = m6
                        k = 6
                    else:
                        H = h7
                        M = m7
                        k = 7
            if a2 == 14:
                    H = h8
                    M = m8


            then = datetime(1, 1, 1, H, M, 0)
            duration = then - now
            duration = str(duration)
            x = duration.split(',')
            x1 = x[1].split(':')
            x = int(x1[1])
            dku_0 = ('До конца', k, 'урока осталось', x, 'минут')
            dku_0 = str(dku_0)
            dku = ''
            for i in dku_0:
                if i != '(' and i != "'" and i != ',' and i != ')':
                    dku += i

            if k == 0:
                last_id = vk_.messages.send(
                        user_id=event.object.user_id,
                        random_id=get_random_id(),
                        peer_id=event.object.peer_id,
                        message= 'Уроков нет'
                )
                f_toggle = not f_toggle

            else:
                last_id = vk_.messages.send(
                            user_id=event.object.user_id,
                            random_id=get_random_id(),
                            peer_id=event.object.peer_id,
                            message= dku
                    )
                f_toggle = not f_toggle

if __name__ == '__main__':
    print()