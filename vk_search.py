import json

import requests
from pprint import pprint

users_params = {
    'count': 10,
    'fields': 'sex, city, bdate, relation',
    'age_from': 25,
    'age_to': 35
}


def search_users_in_vk(users_params_to_search):
    YA_API_BASE_URL = 'https://api.vk.com/method/'
    auth_params = {
        'access_token': '',
        'v': 5.131
    }
    response = requests.get(YA_API_BASE_URL + 'users.search',
                            params={**users_params_to_search, **auth_params})
    #print(response.json())
    founded_users_ids = []
    with open('founded_users.json', 'w', encoding='utf-8') as f:
        json.dump(f'Эрзац база данных найденных людей.\n', f, indent=4, ensure_ascii=False)
    for human in (response.json()['response']['items']):
        founded_users_ids.append(human['id'])
        with open('founded_users.json', 'a', encoding='utf-8') as f:
            json.dump(human, f, indent=4, ensure_ascii=False)
    return founded_users_ids


def get_one_user_photos_urls_list(photos_owner_id):
    #Выдает список ссылок на фото полльзователя с указанным id
    URL = 'https://api.vk.com/method/photos.get'
    params = {
        'owner_id': str(photos_owner_id),
        'album_id': 'profile',
        'access_token': 'a0a9ae4006260db650ede3957f56d61b642f9ef8047f698a79e47ab5f03ff641fd0e56370bd8578002da7',
        'extended': 1,
        'v': '5.131'
    }
    response = requests.get(URL, params=params).json()
    pprint(response)
    user_photos_urls_list = []
    for photo in response['response']['items']:
        max_size = 0
        max_size_url = ''
        for photo_size in photo['sizes']:
            if photo_size['height'] > max_size:
                max_size = photo_size['height']
                max_size_url = photo_size['url']
                max_size_type = photo_size['type']
        user_photos_urls_list.append({'id': photo['id'], 'likes': photo['likes']['count'], 'url': max_size_url})
    return {'owner_id': photos_owner_id, 'items': user_photos_urls_list}
    #return response

