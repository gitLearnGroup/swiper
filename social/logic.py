from user.models import User
from datetime import date
from social.models import Swiped, Friend


def get_rem_user(user):
    location = user.profile.location
    sex = user.profile.dating_sex
    min_dating_age = user.profile.min_dating_age
    max_dating_age = user.profile.max_dating_age

    current_year = date.today().year
    min_birth_year = current_year - int(min_dating_age)
    max_birth_year = current_year - int(max_dating_age)

    result = User.objects.filter(location=location,
                                 sex=sex,
                                 birth_year__gte=max_birth_year,
                                 birth_year__lte=min_birth_year
                                 )
    return result


def like(uid, sid):
    Swiped.mark(uid=uid, sid=sid, status='like')
    match_flag = Swiped.is_liked(sid, uid)
    if match_flag:
        Friend.be_friends(uid, sid)
    return match_flag


def super_like(uid, sid):
    Swiped.mark(uid=uid, sid=sid, status='super_like')
    match_flag = Swiped.is_liked(sid, uid)
    if match_flag:
        Friend.be_friends(uid, sid)
    return match_flag


def dislike(uid, sid):
    Swiped.mark(uid=uid, sid=sid, status='dislike')


def rewind(uid, sid):
    Swiped.mark(uid=uid, sid=sid, status='dislike')
    is_friend = Friend.if_friend(uid, sid)
    if is_friend:
        Friend.break_off(uid, sid)

