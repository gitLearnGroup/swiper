from . import logic
from lib.http import render_response


def get_verify_code(request):
    """用户注册"""
    phone_num = request.POST.get('phonenum', 13619833735)
    logic.send_verify(phone_num)
    return render_response(None, 0)


def login(request):
    """用户登录"""
    pass


def get_profile(request):
    """获取用户资料"""
    pass


def modify_profile(request):
    """修改用户资料"""
    pass


def upload_avatar(request):
    """上传用户头像"""
    pass
