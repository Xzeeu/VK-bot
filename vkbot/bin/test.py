from typing import overload
import vk_api, vk
import json
import datetime
from vk_api import keyboard
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
from vk_api.longpoll import Event, VkLongPoll, VkEventType
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vkbot.bin.maindef import event_m_send, last_m_send

from vkbot.bin.settings import*
from vkbot.bin.keyboard import*


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


def qusend(event, keyboard, message):
    last_id = vk_.messages.send(
                        user_id=event.object.user_id,
                        random_id=get_random_id(),
                        peer_id=event.object.peer_id,
                        keyboard = keyboard,
                        message = message
                )



f_toggle: bool = False

'''Hnature = 0
Htechnics = 0
HH = 0
Hsymbol = 0
Himahe = 0'''


def proftest(event):
    
    qusend(event, keyboard_1.get_keyboard(), 'Пройди тест' )
    qusend(event, keyboard_10.get_keyboard(), 'Какую работу вы предпочтёте? \n 1. Ухаживать за животными \n 2. Обслуживать машины, приборы ' )

Hnature = 0
Htechnics = 0
HH = 0
Hsymbol = 0
Himahe = 0

def aproftest(event):

    global Hnature, Htechnics, HH, Hsymbol ,Himahe

#обработка результатов

    if event.type == VkBotEventType.MESSAGE_EVENT:
        if event.object.payload.get('type') == '01':
            Hnature += 1
            qusend(event, keyboard_11.get_keyboard(), ' 1. Помогать больным людям, лечить их. \n 2. Составлять таблицы, схемы, программы вычислительных машин.')
            
        if event.object.payload.get('type') == '10':
            Htechnics += 1
            qusend(event, keyboard_11.get_keyboard(), ' 1. Помогать больным людям, лечить их. \n 2. Составлять таблицы, схемы, программы вычислительных машин.')

        if event.object.payload.get('type') == '02':
            HH += 1
            qusend(event, keyboard_12.get_keyboard(), ' 1. Следить за качеством книжных иллюстраций, плакатов, художественных открыток, грампластинок. \n 2. Следить за состоянием, развитием растений.')
        if event.object.payload.get('type') == '20':
            Hsymbol += 1
            qusend(event, keyboard_12.get_keyboard(), ' 1. Следить за качеством книжных иллюстраций, плакатов, художественных открыток, грампластинок. \n 2. Следить за состоянием, развитием растений.')

        if event.object.payload.get('type') == '03':
            Himahe += 1
            qusend(event, keyboard_13.get_keyboard(), ' 1. Обрабатывать материалы (дерево, ткань, пластмассу и т.д.). \n 2. Доводить товары до потребителя (рекламировать, продавать).')
        if event.object.payload.get('type') == '30':
            Hnature += 1
            qusend(event, keyboard_13.get_keyboard(), ' 1. Обрабатывать материалы (дерево, ткань, пластмассу и т.д.). \n 2. Доводить товары до потребителя (рекламировать, продавать).')
    
        if event.object.payload.get('type') == '04':
            Htechnics += 1
            qusend(event, keyboard_14.get_keyboard(), ' 1. Обсуждать научно-популярные книги, статьи. \n 2. Обсуждать художественные книги.')
        if event.object.payload.get('type') == '40':
            HH += 1
            qusend(event, keyboard_14.get_keyboard(), ' 1. Обсуждать научно-популярные книги, статьи. \n 2. Обсуждать художественные книги.')

        if event.object.payload.get('type') == '05':
            Htechnics += 1
            qusend(event, keyboard_15.get_keyboard(), ' 1. Выращивать молодняк животных какой-либо породы. \n 2. Тренировать сверстников (или младших) в выполнении каких-либо действий (трудовых, учебных, спортивных).')
        if event.object.payload.get('type') == '50':
            Himahe += 1
            qusend(event, keyboard_15.get_keyboard(), ' 1. Выращивать молодняк животных какой-либо породы. \n 2. Тренировать сверстников (или младших) в выполнении каких-либо действий (трудовых, учебных, спортивных).')

        if event.object.payload.get('type') == '06':
            Hnature += 1
            qusend(event, keyboard_16.get_keyboard(), ' 1. Копировать рисунки, изображения, настраивать музыкальные инструменты. \n 2. Управлять каким-либо грузовым, подъёмным, транспортным средством (подъёмным краном, машиной и т.п.).')
        if event.object.payload.get('type') == '60':
            HH += 1
            qusend(event, keyboard_16.get_keyboard(), ' 1. Копировать рисунки, изображения, настраивать музыкальные инструменты. \n 2. Управлять каким-либо грузовым, подъёмным, транспортным средством (подъёмным краном, машиной и т.п.).')

        if event.object.payload.get('type') == '07':
            Himahe += 1
            qusend(event, keyboard_17.get_keyboard(), ' 1. Сообщать, разъяснять людям нужные для них сведения в справочном бюро, во время экскурсии и т.д. \n 2. Художественно оформлять выставки, витрины, участвовать в подготовке концертов, пьес и т.п.')
        if event.object.payload.get('type') == '70':
            Htechnics += 1
            qusend(event, keyboard_17.get_keyboard(), ' 1. Сообщать, разъяснять людям нужные для них сведения в справочном бюро, во время экскурсии и т.д. \n 2. Художественно оформлять выставки, витрины, участвовать в подготовке концертов, пьес и т.п.')
        
        if event.object.payload.get('type') == '08':
            HH += 1
            qusend(event, keyboard_18.get_keyboard(), ' 1. Ремонтировать изделия, вещи (одежду, технику), жилище. \n 2. Искать и исправлять ошибки в текстах, таблицах, рисунках.')
        if event.object.payload.get('type') == '80':
            Himahe += 1
            qusend(event, keyboard_18.get_keyboard(), ' 1. Ремонтировать изделия, вещи (одежду, технику), жилище. \n 2. Искать и исправлять ошибки в текстах, таблицах, рисунках.')

        if event.object.payload.get('type') == '09':
            Htechnics += 1
            qusend(event, keyboard_19.get_keyboard(), ' 1. Лечить животных. \n 2. Выполнять расчёты, вычисления.')
        if event.object.payload.get('type') == '90':
            Hsymbol += 1
            qusend(event, keyboard_19.get_keyboard(), ' 1. Лечить животных. \n 2. Выполнять расчёты, вычисления.')

        if event.object.payload.get('type') == '100':
            Hnature += 1
            qusend(event, keyboard_20.get_keyboard(), ' 1. Выводить новые сорта растений. \n 2. Конструировать новые виды промышленных изделий (машины, одежду, дома и т.д.).')
        if event.object.payload.get('type') == '010':
            Hsymbol += 1
            qusend(event, keyboard_20.get_keyboard(), ' 1. Выводить новые сорта растений. \n 2. Конструировать новые виды промышленных изделий (машины, одежду, дома и т.д.).')

        if event.object.payload.get('type') == '200':
            Hnature += 1
            qusend(event, keyboard_21.get_keyboard(), ' 1. Разбирать споры, ссоры между людьми, убеждать, разъяснять, поощрять, наказывать. \n 2. Разбираться в чертежах, схемах, таблицах (проверять, уточнять, приводить в порядок).')
        if event.object.payload.get('type') == '020':
            Htechnics += 1
            qusend(event, keyboard_21.get_keyboard(), ' 1. Разбирать споры, ссоры между людьми, убеждать, разъяснять, поощрять, наказывать. \n 2. Разбираться в чертежах, схемах, таблицах (проверять, уточнять, приводить в порядок).')
        
        if event.object.payload.get('type') == '300':
            HH += 1
            qusend(event, keyboard_22.get_keyboard(), ' 1. Наблюдать, изучать работу кружков художественной самодеятельности. \n 2. Наблюдать, изучать жизнь микробов.')
        if event.object.payload.get('type') == '030':
            Hsymbol += 1
            qusend(event, keyboard_22.get_keyboard(), ' 1. Наблюдать, изучать работу кружков художественной самодеятельности. \n 2. Наблюдать, изучать жизнь микробов.')

        if event.object.payload.get('type') == '400':
            Himahe += 1
            qusend(event, keyboard_23.get_keyboard(), ' 1. Обслуживать, налаживать медицинские приборы и аппараты. \n 2. Оказывать людям медицинскую помощь при ранениях, ушибах, ожогах и т.п.')
        if event.object.payload.get('type') == '040':
            Hnature += 1
            qusend(event, keyboard_23.get_keyboard(), ' 1. Обслуживать, налаживать медицинские приборы и аппараты. \n 2. Оказывать людям медицинскую помощь при ранениях, ушибах, ожогах и т.п.')

        if event.object.payload.get('type') == '500':
            Htechnics += 1
            qusend(event, keyboard_24.get_keyboard(), ' 1. Составлять точные описания, отчёты о наблюдаемых явлениях, событиях, измеряемых объектах и др. \n 2. Художественно описывать, изображать события наблюдаемые или представляемые.')
        if event.object.payload.get('type') == '050':
            HH += 1
            qusend(event, keyboard_24.get_keyboard(), ' 1. Составлять точные описания, отчёты о наблюдаемых явлениях, событиях, измеряемых объектах и др. \n 2. Художественно описывать, изображать события наблюдаемые или представляемые.')

        if event.object.payload.get('type') == '600':
            Hsymbol += 1
            qusend(event, keyboard_25.get_keyboard(), ' 1. Делать лабораторные анализы в больнице. \n 2. Принимать, осматривать больных, беседовать с ними, назначать лечение.')
        if event.object.payload.get('type') == '060':
            Himahe += 1
            qusend(event, keyboard_25.get_keyboard(), ' 1. Делать лабораторные анализы в больнице. \n 2. Принимать, осматривать больных, беседовать с ними, назначать лечение.')

        if event.object.payload.get('type') == '700':
            Hnature += 1
            qusend(event, keyboard_26.get_keyboard(), ' 1. Красить или расписывать стены помещений, поверхность изделий. \n 2. Осуществлять монтаж здания или сборку машин, приборов.')
        if event.object.payload.get('type') == '070':
            HH += 1
            qusend(event, keyboard_26.get_keyboard(), ' 1. Красить или расписывать стены помещений, поверхность изделий. \n 2. Осуществлять монтаж здания или сборку машин, приборов.')

        if event.object.payload.get('type') == '800':
            Himahe += 1
            qusend(event, keyboard_27.get_keyboard(), ' 1. Организовывать культ¬ походы людей в театры, музеи, на экскурсии, в туристические путешествия и т.п. \n 2. Играть на сцене, принимать участие в концертах.')
        if event.object.payload.get('type') == '080':
            Htechnics += 1
            qusend(event, keyboard_27.get_keyboard(), ' 1. Организовывать культ¬ походы людей в театры, музеи, на экскурсии, в туристические путешествия и т.п. \n 2. Играть на сцене, принимать участие в концертах.')

        if event.object.payload.get('type') == '900':
            HH += 1
            qusend(event, keyboard_28.get_keyboard(), ' 1. Изготовлять по чертежам детали, изделия (машины, одежду), строить здания. \n 2. Заниматься черчением, копировать карты, чертежи.')
        if event.object.payload.get('type') == '090':
            Himahe += 1
            qusend(event, keyboard_28.get_keyboard(), ' 1. Изготовлять по чертежам детали, изделия (машины, одежду), строить здания. \n 2. Заниматься черчением, копировать карты, чертежи.')

        if event.object.payload.get('type') == '1000':
            Htechnics += 1
            qusend(event, keyboard_29.get_keyboard(), ' 1. Вести борьбу с болезнями растений, с вредителями леса, сада. \n 2. Работать на машинах (пишущая машина, компьютер, телетайп, телефакс).')
        if event.object.payload.get('type') == '1010':
            Hsymbol += 1
            qusend(event, keyboard_29.get_keyboard(), ' 1. Вести борьбу с болезнями растений, с вредителями леса, сада. \n 2. Работать на машинах (пишущая машина, компьютер, телетайп, телефакс).')

        if event.object.payload.get('type') == '2000':
            Hnature += 1
            qusend(event, None,'Результаты тестирования:')
            rezultat(event)
        if event.object.payload.get('type') == '2020':
            Hsymbol += 1
            qusend(event, None,'Результаты тестирования:')
            rezultat(event)



        '''if event.object.payload.get('type') == '04':
            Htechnics += 1
            rezultat(event)
       
        if event.object.payload.get('type') == '40':
            HH += 1
            rezultat(event)'''
            


def rezultat(event):
    global Hnature, Htechnics, HH, Hsymbol ,Himahe

    rez = max(Hnature, Htechnics, HH, Hsymbol ,Himahe)
    if rez == Hnature:
        qusend(event, None, 'Человек — природа. Сюда входят профессии, в которых человек имеет дело с различными явлениями неживой и живой природы, например биолог, географ, геолог, математик, физик, химик и другие профессии, относящиеся к разряду естественных наук.')
    if rez == Htechnics:
        qusend(event, None, 'Человек — техника. В эту группу профессий включены различные виды трудовой деятельности, в которых человек  имеет дело с техникой, её использованием или конструированием, например профессия инженера, оператора, машиниста, механизатора, сварщика и т.п.')
    if rez == HH:
        qusend(event, None, 'Человек — человек. Сюда включены все виды профессий, предполагающих взаимодействие людей, например политика, религия, педагогика, психология, медицина, торговля, право.')
    if rez == Hsymbol:
        qusend(event, None, 'Человек — знаковая система. В эту группу включены профессии, касающиеся создания, изучения и использованияразличных знаковых систем, например лингвистика, языки математического программирования, способы графического представления результатов наблюдений и т.п.')
    if rez == Himahe:
        qusend(event, None, 'Человек — художественный образ. Эта группа профессий представляет собой различные виды художественно-творческого труда, например литература, музыка, театр, изобразительное искусство.')
    
    Hnature = 0
    Htechnics = 0
    HH = 0
    Hsymbol = 0
    Himahe = 0

