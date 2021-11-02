import vk_api, vk
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


vk_session = vk_api.VkApi(token='17e23271daa238193862bc335ee78450a51ae018671bf72a97a32ee736d538041235deb025ae34c329ceb')

GROUP_ID = '207758161'
GROUP_TOKEN = '17e23271daa238193862bc335ee78450a51ae018671bf72a97a32ee736d538041235deb025ae34c329ceb'
API_VERSION = '5.120'

CALLBACK_TYPES = ('show_snackbar', 'open_link', 'open_app')

vk_session = VkApi(token=GROUP_TOKEN, api_version=API_VERSION)
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, group_id=GROUP_ID)