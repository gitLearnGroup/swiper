from django.db import models
from django.db.models import Q
from user.models import User


class Swiped(models.Model):
    """用户数据模型"""
    STATUS = (
        ('dislike', '不喜欢'),
        ('like', '喜欢'),
        ('super_like', '超级喜欢')
    )
    uid = models.IntegerField(verbose_name='滑动着id')
    sid = models.IntegerField(verbose_name='被滑动着id')
    status = models.CharField(choices=STATUS, max_length=10)
    time = models.DateTimeField(auto_now_add=True)

    @classmethod
    def mark(cls, uid, sid, status):
        if status in ['dislike', 'like', 'super_like']:
            cls.objects.update_or_create(uid=uid,
                                         sid=sid,
                                         status=status)

    @classmethod
    def is_liked(cls, uid, sid):
        status = cls.objects.filter(uid=uid, sid=sid, status__in=['like', 'super_like']).exists()
        return status


class Friend(models.Model):
    uid1 = models.IntegerField()
    uid2 = models.IntegerField()

    @classmethod
    def be_friends(cls, uid1, uid2):
        uid1, uid2 = sorted([uid1, uid2])
        cls.objects.get_or_create(uid1=uid1, uid2=uid2)

    @classmethod
    def if_friend(cls, uid1, uid2):
        condition = Q(uid1=uid1, uid2=uid2) | Q(uid1=uid2, uid2=uid1)
        return cls.objects.filter(condition).exists()

    @classmethod
    def break_off(cls, uid1, uid2):
        condition = Q(uid1=uid1, uid2=uid2) | Q(uid1=uid2, uid2=uid1)
        try:
            cls.objects.filter(condition).delete()
        except cls.DoesNotExist:
            pass

    @classmethod
    def select_friend(cls, uid):
        condition = Q(uid1=uid) | Q(uid2=uid)
        friends = cls.objects.filter(condition)
        friend_id_list = []
        for frd in friends:
            user_id = frd.uid2 if frd.uid1 == uid else frd.uid1
            friend_id_list.append(user_id)
        return User.objects.filter(id__in=friend_id_list)
