import vk_api, vk
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


keyboard_1 = VkKeyboard(one_time=False)

keyboard_1.add_callback_button(label='Куда поступать?', color=VkKeyboardColor.POSITIVE, payload={"type": "proftest"})
keyboard_1.add_line()
keyboard_1.add_callback_button(label='Когда ЕГЭ?', color=VkKeyboardColor.POSITIVE, payload={"type": "dataege"})
keyboard_1.add_callback_button(label='Как посутпить в ВУЗ?', color=VkKeyboardColor.POSITIVE, payload={"type": "kakpostupit"})
keyboard_1.add_callback_button(label='Доп. баллы к ЕГЭ', color=VkKeyboardColor.POSITIVE, payload={"type": "dopball"})
keyboard_1.add_line()
keyboard_1.add_callback_button(label='Полезные ресурсы для поступающих', color=VkKeyboardColor.POSITIVE, payload={"type": "polres"})

keyboard_2 = VkKeyboard(one_time=False)
keyboard_2.add_callback_button('Назад', color=VkKeyboardColor.NEGATIVE, payload={"type": "my_own_100500_type_edit"})

f_toggle: bool = False