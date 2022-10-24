from lib.http import render_response
from social import logic
from social.models import Friend
from vip.logic import perm_require
from lib.record import logger


def get_user(request):
    group_num = int(request.GET.get('group_num', 0))
    start = group_num * 5
    end = start + 5
    patch_user = logic.get_rem_user(request.user)
    result = [user.to_dict() for user in patch_user[start:end]]
    if not result: logger.debug(f'group_num的数量为{group_num},超出总匹配数')
    return render_response(result)


def like(request):
    uid = request.user.id
    sid = int(request.POST.get('sid'))
    match_flag = logic.like(uid, sid)
    logger.info(f"用户-{uid} like 用户-{sid}")
    return render_response({'is_match': match_flag})


@perm_require('super_like')
def super_like(request):
    uid = request.user.id
    sid = int(request.POST.get('sid'))
    match_flag = logic.super_like(uid, sid)
    logger.info(f"用户-{uid} super_like 用户-{sid}")
    return render_response({'is_match': match_flag})


def dislike(request):
    uid = request.user.id
    sid = int(request.POST.get('sid'))
    logic.dislike(uid, sid)
    logger.info(f"用户-{uid} dislike 用户-{sid}")
    return render_response(None)


@perm_require('rewind')
def rewind(request):
    uid = request.user.id
    sid = int(request.POST.get('sid'))
    logic.rewind(uid, sid)
    logger.info(f"用户-{uid} rewind 用户-{sid}")
    return render_response(None)


def get_friends(request):
    uid = request.user.id
    friends = Friend.select_friend(uid)
    result = [frd.to_dict() for frd in friends]
    return render_response({'friends': result})

