from django.db import models
from django.core.cache import cache


def get(cls, *args, **kwargs):
    pk = kwargs.get('pk') or kwargs.get('id')
    if pk is not None:
        key = f"models_{cls.__name__}_{pk}"
        models_data = cache.get(key)
        if isinstance(models_data, cls):
            return models_data
        models_data = cls.objects.get(*args, **kwargs)
        cache.set(key, models_data)
        return models_data


def get_or_create(cls, *args, **kwargs):
    pk = kwargs.get('pk') or kwargs.get('id')
    if pk is not None:
        key = f"models_{cls.__name__}_{pk}"
        models_data = cache.get(key)
        if isinstance(models_data, cls):
            return models_data, False
        models_data, created = cls.objects.get_or_create(*args, **kwargs)
        cache.set(key, models_data)
        return models_data, created


def save(self, *args, **kwargs):
    #  此处若为self.pk则即使不用mysql自带的表关系，也要设置主键
    # key = f"models_{self.__class__.__name__}_{self.pk}"
    key = f"models_{self.__class__.__name__}_{self.id}"
    self._origin_save(*args, **kwargs)
    cache.set(key, self)


def patch_model():
    models.Model.get = classmethod(get)
    """当调用models.Model.get()相当于如下：
    models.py文件
    class Model:
        @classmethod
        def get(cls, *args, **kwargs):
            pk = kwargs.get('pk') or kwargs.get('id')
            if pk is not None:
                key = f"models_{cls.__name__}_{pk}"
                models_data = cache.get(key)
                if isinstance(models_data, cls):
                    return models_data
                models_data = cls.objects.get(*args, **kwargs)
                cache.set(key, models_data)
                return models_data
    """
    models.Model.get_or_create = classmethod(get_or_create)

    models.Model._origin_save = models.Model.save
    models.Model.save = save
    """如下例：
        class A:
        def __init__(self):
            self.text = '111111111111'
        def abc(self):
            print(self.text)
                      
    def rt(self):
        print(f"{self.text}22222222222")
         
    if __name__ == '__main__':
        A.abc_old = A.abc
        A.abc = rt
        a = A()
        a.abc()
           
    OUTPUT: 11111111111122222222222  
    """
