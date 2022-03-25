import vk_api, vk
from vk_api.utils import get_random_id
from edbot.settings import vk_


def new_m_send(event, keyboard, message):
    vk_.messages.send(
                        user_id=event.obj.message['from_id'],
                        random_id=get_random_id(),
                        peer_id=event.obj.message['from_id'],
                        keyboard = keyboard,
                        message= message
                )

def event_m_send(event, keyboard, message):
    last_id = vk_.messages.send(
                        user_id=event.object.user_id,
                        random_id=get_random_id(),
                        peer_id=event.object.peer_id,
                        keyboard = keyboard,
                        message= message
                )

def last_m_send(event, keyboard, message):
    last_id = vk_.messages.send(
                        user_id=event.object.user_id,
                        random_id=get_random_id(),
                        peer_id=event.object.peer_id,
                        keyboard = keyboard,
                        message = message
                )