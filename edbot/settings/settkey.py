import vk_api, vk
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


keyboard_10 = VkKeyboard(inline = True, one_time=False)
keyboard_11 = VkKeyboard(inline = True, one_time=False)
keyboard_12 = VkKeyboard(inline = True, one_time=False)
keyboard_13 = VkKeyboard(inline = True, one_time=False)
keyboard_14 = VkKeyboard(inline = True, one_time=False)
keyboard_15 = VkKeyboard(inline = True, one_time=False)
keyboard_16 = VkKeyboard(inline = True, one_time=False)
keyboard_17 = VkKeyboard(inline = True, one_time=False)
keyboard_18 = VkKeyboard(inline = True, one_time=False)
keyboard_19 = VkKeyboard(inline = True, one_time=False)
keyboard_20 = VkKeyboard(inline = True, one_time=False)
keyboard_21 = VkKeyboard(inline = True, one_time=False)
keyboard_22 = VkKeyboard(inline = True, one_time=False)
keyboard_23 = VkKeyboard(inline = True, one_time=False)
keyboard_24 = VkKeyboard(inline = True, one_time=False)
keyboard_25 = VkKeyboard(inline = True, one_time=False)
keyboard_26 = VkKeyboard(inline = True, one_time=False)
keyboard_27 = VkKeyboard(inline = True, one_time=False)
keyboard_28 = VkKeyboard(inline = True, one_time=False)
keyboard_29 = VkKeyboard(inline = True, one_time=False)
keyboard_30 = VkKeyboard(inline = True, one_time=False)


keyboard_10.add_callback_button(label='1.', color=VkKeyboardColor.POSITIVE, payload={"type": "01"})
keyboard_10.add_callback_button(label='2.', color=VkKeyboardColor.POSITIVE, payload={"type": "10"})

keyboard_11.add_callback_button(label='1', color=VkKeyboardColor.POSITIVE, payload={"type": "02"})
keyboard_11.add_callback_button(label='2', color=VkKeyboardColor.POSITIVE, payload={"type": "20"})

keyboard_12.add_callback_button(label='1', color=VkKeyboardColor.POSITIVE, payload={"type": "03"})
keyboard_12.add_callback_button(label='2', color=VkKeyboardColor.POSITIVE, payload={"type": "30"})

keyboard_13.add_callback_button(label='1', color=VkKeyboardColor.POSITIVE, payload={"type": "04"})
keyboard_13.add_callback_button(label='2', color=VkKeyboardColor.POSITIVE, payload={"type": "40"})

keyboard_14.add_callback_button(label='1', color=VkKeyboardColor.POSITIVE, payload={"type": "05"})
keyboard_14.add_callback_button(label='2', color=VkKeyboardColor.POSITIVE, payload={"type": "50"})

keyboard_15.add_callback_button(label='1', color=VkKeyboardColor.POSITIVE, payload={"type": "06"})
keyboard_15.add_callback_button(label='2', color=VkKeyboardColor.POSITIVE, payload={"type": "60"})

keyboard_16.add_callback_button(label='1', color=VkKeyboardColor.POSITIVE, payload={"type": "07"})
keyboard_16.add_callback_button(label='2', color=VkKeyboardColor.POSITIVE, payload={"type": "70"})

keyboard_17.add_callback_button(label='1', color=VkKeyboardColor.POSITIVE, payload={"type": "08"})
keyboard_17.add_callback_button(label='2', color=VkKeyboardColor.POSITIVE, payload={"type": "80"})

keyboard_18.add_callback_button(label='1', color=VkKeyboardColor.POSITIVE, payload={"type": "09"})
keyboard_18.add_callback_button(label='2', color=VkKeyboardColor.POSITIVE, payload={"type": "90"})

keyboard_19.add_callback_button(label='1', color=VkKeyboardColor.POSITIVE, payload={"type": "100"})
keyboard_19.add_callback_button(label='2', color=VkKeyboardColor.POSITIVE, payload={"type": "010"})

keyboard_20.add_callback_button(label='1', color=VkKeyboardColor.POSITIVE, payload={"type": "200"})
keyboard_20.add_callback_button(label='2', color=VkKeyboardColor.POSITIVE, payload={"type": "020"})

keyboard_21.add_callback_button(label='1', color=VkKeyboardColor.POSITIVE, payload={"type": "300"})
keyboard_21.add_callback_button(label='2', color=VkKeyboardColor.POSITIVE, payload={"type": "030"})

keyboard_22.add_callback_button(label='1', color=VkKeyboardColor.POSITIVE, payload={"type": "400"})
keyboard_22.add_callback_button(label='2', color=VkKeyboardColor.POSITIVE, payload={"type": "040"})

keyboard_23.add_callback_button(label='1', color=VkKeyboardColor.POSITIVE, payload={"type": "500"})
keyboard_23.add_callback_button(label='2', color=VkKeyboardColor.POSITIVE, payload={"type": "050"})

keyboard_24.add_callback_button(label='1', color=VkKeyboardColor.POSITIVE, payload={"type": "600"})
keyboard_24.add_callback_button(label='2', color=VkKeyboardColor.POSITIVE, payload={"type": "060"})

keyboard_25.add_callback_button(label='1', color=VkKeyboardColor.POSITIVE, payload={"type": "700"})
keyboard_25.add_callback_button(label='2', color=VkKeyboardColor.POSITIVE, payload={"type": "070"})

keyboard_26.add_callback_button(label='1', color=VkKeyboardColor.POSITIVE, payload={"type": "800"})
keyboard_26.add_callback_button(label='2', color=VkKeyboardColor.POSITIVE, payload={"type": "080"})

keyboard_27.add_callback_button(label='1', color=VkKeyboardColor.POSITIVE, payload={"type": "900"})
keyboard_27.add_callback_button(label='2', color=VkKeyboardColor.POSITIVE, payload={"type": "090"})

keyboard_28.add_callback_button(label='1', color=VkKeyboardColor.POSITIVE, payload={"type": "1000"})
keyboard_28.add_callback_button(label='2', color=VkKeyboardColor.POSITIVE, payload={"type": "1010"})

keyboard_29.add_callback_button(label='1', color=VkKeyboardColor.POSITIVE, payload={"type": "2000"})
keyboard_29.add_callback_button(label='2', color=VkKeyboardColor.POSITIVE, payload={"type": "2020"})

keyboard_30.add_callback_button(label='1', color=VkKeyboardColor.POSITIVE, payload={"type": "800"})
keyboard_30.add_callback_button(label='2', color=VkKeyboardColor.POSITIVE, payload={"type": "080"})