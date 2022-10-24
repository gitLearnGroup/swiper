from django.db import models


class Vip(models.Model):
    name = models.CharField(max_length=10)
    level = models.IntegerField()
    price = models.FloatField()

    def perms(self):
        perm_ids = VipPermRelative.objects.filter(vip_id=self.id).values_list('perm_id')
        result = Permission.objects.filter(id__in=perm_ids)
        return result

    def has_perm(self, perm_name):
        perm_id = Permission.objects.get(name=perm_name).id
        return VipPermRelative.objects.filter(vip_id=self.id, perm_id=perm_id).exists()


class Permission(models.Model):
    name = models.CharField(max_length=20)


class VipPermRelative(models.Model):
    vip_id = models.IntegerField()
    perm_id = models.IntegerField()
