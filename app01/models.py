from django.db import models


class ServerInfos(models.Model):
    datetime = models.DateTimeField(verbose_name="创建时间")
    port = models.IntegerField()
    server_name = models.CharField(max_length=32, unique=True)
    username = models.CharField(max_length=32)
    ip_addr = models.GenericIPAddressField(unique=True)
    auth = models.CharField(max_length=16, default="password")
    pkey = models.TextField(null=True, blank=True)
    password = models.CharField(max_length=180, null=True, blank=True)
    # uptime = models.IntegerField(verbose_name="开机运行时间")

    status_choices = (
        (1, '在线'),
        (2, '宕机'),
        (3, '网络不可达'),
        (4, '下线'),
    )
    status = models.IntegerField(u'状态', choices=status_choices, default=1)
    memo = models.TextField(u'备注', blank=True, null=True)

    class Meta:
        verbose_name = "服务器信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.server_name


class HostTmp(models.Model):
    datetime = models.DateTimeField(auto_now=True)
    unique = models.CharField(max_length=40, unique=True)
    host = models.CharField(max_length=32)
    port = models.IntegerField()
    user = models.CharField(max_length=32)
    auth = models.CharField(max_length=16)
    pkey = models.TextField(null=True, blank=True)
    password = models.CharField(max_length=180, null=True, blank=True)
