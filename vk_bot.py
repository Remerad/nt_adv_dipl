# -*- coding: utf-8 -*-
import time

import requests
from vk_api import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_search import get_one_user_photos_urls_list
import random
from pprint import pprint
import datetime as dt
from dateutil.relativedelta import relativedelta #pip install python-dateutil
from vk_search import search_users_in_vk


def get_full_years(str_bdata):
    first_str = str_bdata.split(".")
    first = dt.datetime(int(first_str[2]), int(first_str[1]), int(first_str[0]))
    return relativedelta(dt1=dt.datetime.now(), dt2=first).years


def male_female_or_none(sex):
    if sex == 1:
        return "женский"
    elif sex == 1:
        return "мужской"
    else:
        return "не указан"


def get_params_for_search(dict_of_client_params):
    # Данная функция делает массив данных для поиска в ВК на основе данных цели
    keys_list = dict_of_client_params.keys()
    dict_of_targets_params = {}
    if "sex" in keys_list:
        if dict_of_client_params["sex"] == 1:
            dict_of_targets_params.update({"sex": 2})
        elif dict_of_client_params["sex"] == 2:
            dict_of_targets_params.update({"sex": 1})
    if "bdate" in keys_list:
        dict_of_targets_params.update({'age_from': get_full_years(dict_of_client_params["bdate"])-5,
                                       'age_to': get_full_years(dict_of_client_params["bdate"])+5
                                       })
    if "city" in keys_list:
        dict_of_targets_params.update({'city': dict_of_client_params["city"]["id"]})
    dict_of_targets_params.update({'count': 10, 'fields': 'bdate, relation'})
    #pprint(dict_of_targets_params)
    return dict_of_targets_params


def make_target_params_str(dict_of_targets_params):
    res_str = "Человека с какими параметрами ищем:"
    if "sex" in dict_of_targets_params.keys():
        if dict_of_targets_params["sex"] == 1:
            res_str += "\nженского пола"
        elif dict_of_targets_params["sex"] == 2:
            res_str += "\nмужского пола"
    else:
        res_str += "\nпол не важен"
    if "age_from" in dict_of_targets_params.keys() and "age_to" in dict_of_targets_params.keys():
        res_str += f";\nвозраст от {dict_of_targets_params['age_from']} до {dict_of_targets_params['age_to']}"
    if "city" in dict_of_targets_params.keys():
        res_str += f"\nгород: {dict_of_targets_params['city']}"
    res_str += "."
    return res_str


class VKBot:
    def __init__(self, vk_group_token):
        self.token = vk_group_token
        self.vk_session = vk_api.VkApi(token=self.token)
        #'')

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

    def wait_for_user(self):
        vk = self.vk_session.get_api()
        longpoll = VkLongPoll(self.vk_session)
        print('Бот ждёт пользователя.')
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                print(f'{event.user_id} прислал сообщение: "{event.text}"')
                if event.text.lower() == 'мне':
                    user_data = self.get_user_data(event.user_id)
                    print(event.user_id)

                    if event.from_user:
                        vk.messages.send(
                            user_id=event.user_id,
                            message=f'Итак, что мы знаем:'
                                    f'\nВаш user_id:{event.user_id}'
                                    f'\nВам {get_full_years(user_data["bdate"])} полных лет'
                                    f'\nВаш пол: {male_female_or_none(user_data["sex"])}'
                                    f'\nВаш город: {user_data["city"]["title"]}',
                            random_id=random.randint(1, 10**7)
                        )
                        vk.messages.send(
                            user_id=event.user_id,
                            message=make_target_params_str(get_params_for_search(user_data)),
                            random_id=random.randint(1, 10 ** 7)
                        )
                        vk.messages.send(
                            user_id=event.user_id,
                            message='Проводим поиск по ВК',
                            random_id=random.randint(1, 10 ** 7)
                        )
                        print("\nСписок ссылок на фото:")
                        i=0
                        for target in search_users_in_vk(get_params_for_search(user_data)):
                            pprint(get_one_user_photos_urls_list(target))
                            time.sleep(0.3)
                            print(i)
                            i += 1
                        #pprint(self.get_user_data(event.user_id))
                else:
                    if event.from_user:
                        vk.messages.send(
                            user_id=event.user_id,
                            message=f'id цели: {event.text}',
                            random_id=random.randint(1, 10 ** 7)
                        )
                        pprint(self.get_user_data(event.user_id))

print(get_full_years("14.7.1989"))
