from common import error
from lib.http import render_response
from lib.record import logger


def perm_require(perm_name):
    def deco(api_func):
        def wrap(request):
            user = request.user
            if user.vip.has_perm(perm_name):
                result = api_func(request)
                return result
            else:
                logger.error(f"用户-{user.id}没有权限：{perm_name}")
                return render_response(None, error.NOT_HAS_PERM)
        return wrap
    return deco
