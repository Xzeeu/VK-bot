import vk_api, vk
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
vk_session = vk_api.VkApi(token='17e23271daa238193862bc335ee78450a51ae018671bf72a97a32ee736d538041235deb025ae34c329ceb')

import knopki

from vk_api.longpoll import VkLongPoll, VkEventType

Lslongpoll = VkLongPoll(vk_session)
Lsvk = vk_session.get_api()

for event in Lslongpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        vars1 = ['Привет', 'Ку', 'Хай', 'Хеллоу']
        if event.text in vars1:
            if event.from_user:
                Lsvk.messages.send(
                    user_id = event.user_id,
                    message = 'Привет)',
                    random_id = get_random_id()
                    )
