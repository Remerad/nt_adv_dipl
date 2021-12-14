from  vk_search import get_one_user_photos_urls_list
from pprint import pprint
from vk_api import VkApi
from vk_api.upload import VkUpload
from vk_api.utils import get_random_id


TOKEN = ''
PEER_ID = 231029


def upload_photo(upload, photo):
    response = upload.photo_messages(photo)[0]

    owner_id = response['owner_id']
    photo_id = response['id']
    access_key = response['access_key']

    return owner_id, photo_id, access_key


def send_photo(vk, peer_id, owner_id, photo_id, access_key):
    attachment = f'photo{owner_id}_{photo_id}_{access_key}'
    vk.messages.send(
        random_id=get_random_id(),
        peer_id=peer_id,
        attachment=attachment
    )



vk_session = VkApi(token=TOKEN)
vk = vk_session.get_api()
upload = VkUpload(vk)

send_photo(vk, PEER_ID, *upload_photo(upload, 'https://sun1-30.userapi.com/impf/uoBkxgFdDog7750_NGWTqqXB-EXWmHEBLZ7GLA/3dUyjLmqulE.jpg?size=300x305&quality=96&sign=a833cc69e8cfbfebd7c4371ce1ba3277&c_uniq_tag=g7PAFsROfy41602-wXim7iJ7tZEbhqJ063g0oGfibpQ&type=album'))



#print(get_photo_urls_list(231029))
# k = get_one_user_photos_urls_list(231029)
# print(len(k))
# pprint(k)

# k = [1,2,3,4,5,6,7]
# list_to_be_sorted = {'items': [{'id': 203603938,
#             'likes': 22,
#             'url': 'https://sun9-3.userapi.com/c9461/u1797838/-6/z_a8e895a1.jpg'},
#            {'id': 268433360,
#             'likes': 22,
#             'url': 'https://sun9-19.userapi.com/c5177/u1797838/-6/w_fe53ded1.jpg'},
#            {'id': 276500517,
#             'likes': 43,
#             'url': 'https://sun9-23.userapi.com/c11437/u1797838/-6/w_1eded50b.jpg'},
#            {'id': 279002102,
#             'likes': 20,
#             'url': 'https://sun9-29.userapi.com/c10116/u1797838/-6/w_9a2945ec.jpg'},
#            {'id': 287983579,
#             'likes': 25,
#             'url': 'https://sun9-37.userapi.com/impf/CjLNxj1kUB0QK25GMnBkVF-L2TwHtd4Cfe7M-w/76DCOpBr_hg.jpg?size=1069x2048&quality=96&sign=b2dfd6ae6898707d5c47f259644cfe42&c_uniq_tag=FqmUk36YtBOEMrCAttONmYJsT8qMvS1ttix_pjigQUU&type=album'},
#            {'id': 291669274,
#             'likes': 13,
#             'url': 'https://sun9-33.userapi.com/impf/X7Nb5Uo3hHkFjJOH8E7UVaAWsporU3wgP9cSdA/-EdYlVlKGYI.jpg?size=640x640&quality=96&sign=777239c15d62fa51423add35aa3962ab&c_uniq_tag=3-Xwg437jKfSW3Db8kVSyNh3j3Zn_MO50mdIdnQ5srQ&type=album'},
#            {'id': 320123069,
#             'likes': 28,
#             'url': 'https://sun9-83.userapi.com/impf/4Z32uO80vgO0YbucxIrYtFesDKYo2lO3YdX9AQ/y_WVbVpj54Q.jpg?size=453x604&quality=96&sign=5f7574cf7f0ac7bf031d389f4deab49f&c_uniq_tag=A_L_V898GLtSM8sSWJ4WIsrXAuksicqiQoItF_ZfJFs&type=album'},
#            {'id': 334202270,
#             'likes': 78,
#             'url': 'https://sun9-8.userapi.com/impf/kBMAtjGeTU71Dtcv8-UkvbxRyd1UuSI1C8AP6w/RfYiYSjOFs8.jpg?size=960x1280&quality=96&sign=b7ca2e42ff0483d56288d247b0c5c7de&c_uniq_tag=sYQzwHvMazse0b_t5qSPXQa6wUHxdnOCnmH40EB3ZgM&type=album'}],
#  'owner_id': 1797838}
# 9
#
# print(k[:3])
# newlist = sorted(list_to_be_sorted['items'], key=lambda k: k['likes'], reverse=True)[:3]
# pprint(newlist)
