from vk_api import VkApi
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import json
from datetime import datetime

now  = datetime.now()

GROUP_ID = '207758161'
GROUP_TOKEN = '17e23271daa238193862bc335ee78450a51ae018671bf72a97a32ee736d538041235deb025ae34c329ceb'
API_VERSION = '5.120'

CALLBACK_TYPES = ('show_snackbar', 'open_link', 'open_app')

vk_session = VkApi(token=GROUP_TOKEN, api_version=API_VERSION)
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, group_id=GROUP_ID)

settings = dict(one_time=False, inline=False)

keyboard_1 = VkKeyboard(**settings)
keyboard_1.add_callback_button(label='Расписание уроков', color=VkKeyboardColor.SECONDARY, payload={"type": "callback"})
keyboard_1.add_line()
keyboard_1.add_callback_button(label='Хороший сайт, там вузы есть', color=VkKeyboardColor.POSITIVE, payload={"type": "open_link", "link": "https://postupi.online/"})
keyboard_1.add_line()



keyboard_1.add_callback_button(label='ещё одно меню если надо будет', color=VkKeyboardColor.NEGATIVE, payload={"type": "my_own_100500_type_edit"})
keyboard_2 = VkKeyboard(**settings)
keyboard_2.add_callback_button('Назад', color=VkKeyboardColor.NEGATIVE, payload={"type": "my_own_100500_type_edit"})

f_toggle: bool = False

'''if datetime.datetime.today().isoweekday() == 7:
    rasp = '1.Физика\n2.Физика\nРусский\nМатематика\nМатематика\nАнглийский\nФизкультура\nФизкультура'''



for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.obj.message['text'] == 'Начать':
            if event.from_user:
                if 'callback' not in event.obj.client_info['button_actions']:
                    print(f'Клиент {event.obj.message["from_id"]} не поддерж. callback')

                vk.messages.send(
                        user_id=event.obj.message['from_id'],
                        random_id=get_random_id(),
                        peer_id=event.obj.message['from_id'],
                        keyboard=keyboard_1.get_keyboard(),
                        message= 'Привет!😊) Если ты не определился чем хочешь заниматься в будущем🤷‍♂️, куда поступать👩‍🎓, то этот бот тебе поможет!'
                )

    elif event.type == VkBotEventType.MESSAGE_EVENT:
        if event.object.payload.get('type') in CALLBACK_TYPES:
            r = vk.messages.sendMessageEventAnswer(
                      event_id=event.object.event_id,
                      user_id=event.object.user_id,
                      peer_id=event.object.peer_id,                                                   
                      event_data=json.dumps(event.object.payload))




        elif event.object.payload.get('type') == 'callback':
            last_id = vk.messages.send(
                        user_id=event.object.user_id,
                        random_id=get_random_id(),
                        peer_id=event.object.peer_id,
                        message= now
                )
            f_toggle = not f_toggle

if __name__ == '__main__':
    print()