import requests
from vk_api import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random
from pprint import pprint

vk_session = vk_api.VkApi(token='09b1de1eb574c8ca1bef2723dc95db3f04cade9238e7521c5bb5e593d82c57d00bb23cc3cc4019f893ee4')
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        # print(f'type(event) - {type(event)}')
        # print(f'event.from_user - {event.from_user}')
        # print(f'event.raw - {event.raw}')
        #
        # print(f'event.from_user - {event.from_user}')
        # print(f'event.from_chat - {event.from_chat}')
        # print(f'event.from_group - {event.from_group}')
        # print(f'event.from_me - {event.from_me}')
        # print(f'event.to_me - {event.to_me}')
        #
        # print(f'event.attachments - {event.attachments}')
        # print(f'event.message_data - {event.message_data}')
        #
        # print(f'event.message_id - {event.message_id}')
        # print(f'event.timestamp - {event.timestamp}')
        # print(f'event.peer_id - {event.peer_id}')
        # print(f'event.flags - {event.flags}')
        # print(f'event.extra - {event.extra}')
        # print(f'event.extra_values - {event.extra_values}')
        # print(f'event.type_id - {event.type_id}')
        print((f'event.user_id - {event.user_id}'))

        url = 'https://api.vk.com/method/'
        users_info_url = url + 'users.get'
        users_info_params = {
            'user_ids': event.user_id,
            'fields': 'sex, bdate, city, relation, country'
        }
        params = {
            'access_token': '09b1de1eb574c8ca1bef2723dc95db3f04cade9238e7521c5bb5e593d82c57d00bb23cc3cc4019f893ee4',
            'v': 5.131
        }
        response = requests.get(users_info_url, params={**params, **users_info_params})
        pprint(response.text)


   #Слушаем longpoll, если пришло сообщение то:

        if event.text == 'Первый вариант фразы' or event.text == 'Второй вариант фразы': #Если написали заданную фразу
            if event.from_user: #Если написали в ЛС
                vk.messages.send( #Отправляем сообщение
                    user_id=event.user_id,
                    message='Ваш текст',
                    random_id=random.randint(10 ** 7)
                )
            elif event.from_chat: #Если написали в Беседе
                vk.messages.send( #Отправляем собщение
                    chat_id=event.chat_id,
                    message='Ваш текст',
                    random_id=random.randint(0, 9999)
                )

    def get_user_data(self, user_id):
        url = 'https://api.vk.com/method/'
        users_info_url = url + 'users.get'
        users_info_params = {
            'user_ids': user_id,
            'fields': 'sex, bdate, city, relation, country'
        }
        params = {
            'access_token': self.token,
            'v': 5.131
        }
        response = requests.get(users_info_url, params={**params, **users_info_params})
        pprint(response.json()['response'][0])
        return response.json()['response'][0]