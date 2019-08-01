from django.db import models


class info(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    addr = models.CharField(max_length=128)

    @classmethod
    def getinfoData(self):
        return dict(system_setup=info.objects.last())


class telNumber(models.Model):
    tel = models.IntegerField()