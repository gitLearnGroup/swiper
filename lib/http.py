import json
from django.shortcuts import HttpResponse
from swiper.settings import DEBUG


def render_response(data, code=0):
    result = {
        'code': code,
        'data': data
    }
    if DEBUG:
        context = json.dumps(result, ensure_ascii=False, indent=4, sort_keys=True)
    else:
        context = json.dumps(result, ensure_ascii=False, separators=(',', ':', ))
    return HttpResponse(context)
