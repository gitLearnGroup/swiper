from random import randrange
from swiper import config
from django.core.cache import cache
from worker import call_by_worker, celery_app
from django.conf import settings
import os


def make_verify(length):
    return randrange(10**(length-1), 10**length)


@call_by_worker
def send_verify(phone_num='13619833735'):
    verify = make_verify(6)
    print(f'生成的验证码: {verify}')
    cache.set(f"verify-{phone_num}", verify, 600)
    data = config.HY_SMS_PARAMS.copy()
    data['mobile'] = phone_num
    data['content'] = data['content'] % verify
    response = {'name': 'lqk'}
    # response = requests.post(config.HY_SMS_URL, data)
    # print(response.json())
    return response


@call_by_worker
def check_verify(v_code, phone_num):
    key = f"verify-{phone_num}"
    verify_code = cache.get(key)
    return verify_code == v_code


def save_avatar(user, file):
    file_dir = os.path.join(settings.BASE_DIR, settings.MEDIA_URL)
    if not os.path.exists(file_dir): os.mkdir(file_dir)
    upload_file_name = f"avatar_{user.id}"
    file_path = os.path.join(file_dir, upload_file_name)
    # file_path = r'D:\Desktop\lqk\PyLearn\Django\project\swiper\media\avatar_2'
    with open(file_path, 'wb') as f:
        for chunk in file.chunks():
            f.write(chunk)
    return file_path, upload_file_name
