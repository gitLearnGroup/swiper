from . import logic
from lib.http import render_response
from .logic import check_verify, save_avatar
from .models import User
from common import error
from user.forms import ProfileForm
from lib.qncloud import async_upload_to_qiniu
from swiper import config
import os


def get_verify_code(request):
    """用户注册"""
    phone_num = request.POST.get('phonenum', 13619833735)
    print(phone_num)
    logic.send_verify(phone_num)
    return render_response(None, 0)


def login(request):
    """用户登录"""
    phone_num = request.POST.get('phonenum')
    v_code = request.POST.get('vcode')
    if check_verify(v_code, phone_num):
        user, created = User.objects.get_or_create(phonenum=phone_num)
        request.session['uid'] = user.id
        data = user.to_dict()
        return render_response(data, 0)
    else:
        return render_response(None, error.NO_VERIFY_CODE)


def get_profile(request):
    """获取用户资料"""
    user = request.user
    profile = user.profile
    return render_response(profile.to_dict())


def modify_profile(request):
    """修改用户资料"""
    form = ProfileForm(request.POST)
    if form.is_valid():
        user = request.user
        user.profile.__dict__.update(form.cleaned_data)
        user.profile.save()
        return render_response(None)
    return render_response(form.errors, error.FORM_ERROR)


def upload_avatar(request):
    """上传用户头像"""
    # 用户上传头像接收
    file = request.FILES.get('avatar')
    if file:
        # file_name = file.name
        user = request.user
        # 用户头像本地保存
        file_path, upload_file_name = save_avatar(user, file)

        # 用户头像从本地上传至七牛云
        async_upload_to_qiniu(file_path, upload_file_name)

        # 把头像在七牛云上的url存入数据库
        qn_url = f"{config.BASE_URL}/{upload_file_name}"
        user.avatar = qn_url
        user.save()
        return render_response(None)
    else:
        return render_response(None, error.NOT_EXIST_FILE)

