from django.shortcuts import render, HttpResponse
from app01 import models
# Create your views here.
from django.views.generic.base import View
from utils.mixin_utils import LoginRequiredMixin
import json
from django.core.serializers.json import DjangoJSONEncoder
from system.models import SystemSetup
from rbac.models import Menu
from django.shortcuts import get_object_or_404


class App02List(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'app02/App02List.html', locals())


from app01 import models


# 服务器详细信息
class App02ListShixian(LoginRequiredMixin, View):

    def get(self, request):
        fields = ['id', 'server_name', 'ip_addr', 'status', 'memo']
        filters = dict()
        osinfo_list = dict(data=list(models.ServerInfos.objects.filter(**filters).values(*fields)))
        return HttpResponse(json.dumps(osinfo_list, cls=DjangoJSONEncoder), content_type='application/json')
