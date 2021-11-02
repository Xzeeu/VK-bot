import vk_api, vk
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from settings import*

settings = dict(one_time=False, inline=False)

error = False
error_el = ''

keyboard_1 = VkKeyboard(**settings)

keyboard_1.add_callback_button(label='Время до конца урока', color=VkKeyboardColor.SECONDARY, payload={"type": "callback"})
keyboard_1.add_line()

keyboard_1.add_callback_button(label='Хороший сайт, там вузы есть', color=VkKeyboardColor.POSITIVE, payload={"type": "open_link", "link": "https://postupi.online/"})
keyboard_1.add_line()

keyboard_1.add_callback_button(label='Сообщить об ошибке', color=VkKeyboardColor.NEGATIVE, payload={"type": "error"})
keyboard_2 = VkKeyboard(**settings)

keyboard_2.add_callback_button('Назад', color=VkKeyboardColor.NEGATIVE, payload={"type": "my_own_100500_type_edit"})

f_toggle: bool = False