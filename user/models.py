from django.db import models
from datetime import date


class User(models.Model):
    """用户数据模型"""
    SEX = (
        ('男', '男'),
        ('女', '女')
    )
    nickname = models.CharField(max_length=18, unique=True)
    phonenum = models.CharField(max_length=12, unique=True)
    sex = models.CharField(default='男', choices=SEX, max_length=8)
    avatar = models.CharField(max_length=32)
    location = models.CharField(max_length=32)
    birth_year = models.IntegerField(default=2000)
    birth_month = models.IntegerField(default=1)
    birth_day = models.IntegerField(default=1)

    @property
    def age(self):
        today = date.today()
        birth_time = date(self.birth_year, self.birth_month, self.birth_day)
        return (today - birth_time).days // 365

    @property
    def profile(self):
        """自定义的数据库表关联"""
        if hasattr(self, '_profile'):
            _profile, _ = Profile.objects.get_or_create(id=self.id)
            self._profile = _profile
        return self._profile


class Profile(models.Model):
    """用户配置项"""
    SEX = (
        ('男', '男'),
        ('女', '女')
    )
    location = models.CharField(max_length=32, verbose_name='目标城市')
    min_distance = models.IntegerField(verbose_name='最小查询范围')
    max_distance = models.IntegerField(verbose_name='最大查询范围')
    min_dating_age = models.CharField(default=18, max_length=3, verbose_name='最小匹配年龄')
    max_dating_age = models.CharField(default=45, max_length=3, verbose_name='最大匹配年龄')
    dating_sex = models.CharField(default='女', choices=SEX, max_length=8)
    vibration = models.BooleanField(default=True, verbose_name='是否开启震动')
    only_match = models.BooleanField(default=True, verbose_name='不让未匹配的人看相册')
    auto_play = models.BooleanField(default=True, verbose_name='自动播放视频')