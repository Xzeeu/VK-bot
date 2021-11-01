import vk_api, vk
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


settings = dict(one_time=False, inline=False)
settings_2 = dict(one_time=False, inline=True)



keyboard_1 = VkKeyboard(**settings)

keyboard_1.add_callback_button(label='Время до конца урока', color=VkKeyboardColor.POSITIVE, payload={"type": "callback"})
keyboard_1.add_line()
keyboard_1.add_callback_button(label='ДЗ', color=VkKeyboardColor.POSITIVE, payload={"type": "dz"})
keyboard_1.add_line()
keyboard_1.add_callback_button(label='Хороший сайт, там вузы есть', color=VkKeyboardColor.SECONDARY, payload={"type": "open_link", "link": "https://postupi.online/"})
keyboard_1.add_line()
keyboard_1.add_callback_button(label='Сообщить об ошибке', color=VkKeyboardColor.NEGATIVE, payload={"type": "error"})

keyboard_2 = VkKeyboard(**settings)
keyboard_2.add_callback_button('Назад', color=VkKeyboardColor.NEGATIVE, payload={"type": "my_own_100500_type_edit"})

keyboard_3 = VkKeyboard(**settings_2)
keyboard_3.add_callback_button(label='Добавить', color=VkKeyboardColor.NEGATIVE, payload={"type": "+dz"})

keyboard_4 = VkKeyboard(**settings_2)
keyboard_4.add_callback_button(label='Удалить', color=VkKeyboardColor.NEGATIVE, payload={"type": "error_del"})

f_toggle: bool = False