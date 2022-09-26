from random import randrange
import requests
from swiper import config
from django.core.cache import cache
from worker import call_by_worker, celery_app


def make_verify(length):
    return randrange(10**(length-1), 10**length)


@call_by_worker
def send_verify(phone_num='13619833735'):
    verify = make_verify(6)
    cache.set(f"verify-{phone_num}", verify, 120)
    data = config.HY_SMS_PARAMS.copy()
    data['mobile'] = phone_num
    data['content'] = data['content'] % verify
    response = {'name': 'lqk'}
    # response = requests.post(config.HY_SMS_URL, data)
    # print(response.json())
    return response
