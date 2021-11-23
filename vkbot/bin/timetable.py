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

def tt(event):
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
            '''x = int(x1[1])
            dku_0 = ('До конца', k, 'урока осталось', x, 'минут')
            dku_0 = str(dku_0)
            dku = ''
            for i in dku_0:
                if i != '(' and i != "'" and i != ',' and i != ')':
                    dku += i'''
            x = int(x1[1])

            #влад молодец
            v223 = x
            if v223 != 11 and v223 % 10 == 1:
                v224 = 'минута'
            elif 4 < v223 < 21 or 5 <= v223 % 10 <= 9:
                v224 = 'минут'
            elif 2<= v223 % 10 <= 4 and 12 != v223 and 13 != v223 and 14 != v223:
                v224 = 'минуты'
            ###
            dku_0 = ('До конца', k, 'урока осталось', x, v224)
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
                        keyboard = keyboard_1.get_keyboard(),
                        message= 'Уроков нет'
                )
                #f_toggle = not f_toggle

            else:
                last_id = vk_.messages.send(
                            user_id=event.object.user_id,
                            random_id=get_random_id(),
                            peer_id=event.object.peer_id,
                            keyboard = keyboard_1.get_keyboard(),
                            message= dku
                    )
                #f_toggle = not f_toggle

            return