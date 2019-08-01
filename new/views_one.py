from .models import info, telNumber
from utils.mixin_utils import LoginRequiredMixin
from rbac.models import Menu
import json
import re
from django.views.generic.base import View
from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.core.serializers.json import DjangoJSONEncoder
from new.models import info, telNumber

from new import models

from system.models import SystemSetup


# 项目管理-用户信息-查看
class xiangmuGuanli(LoginRequiredMixin, View):

    def get(self, request):
        ret = Menu.getMenuByRequestUrl(url=request.path_info)
        ret.update(SystemSetup.getSystemSetupLastData())
        return render(request, 'new/xiangmuguanli_list.html', ret)


class xiangmuGuanliViewList(LoginRequiredMixin, View):

    def get(self, request):
        fields = ['id', 'name', 'addr', 'age']
        ret = dict(data=list(models.info.objects.values(*fields)))
        return HttpResponse(json.dumps(ret, cls=DjangoJSONEncoder), content_type="application/json")


from .forms import NewUpdateForm
from .models import info


# 项目管理-用户信息-修改
class xiangmuGuanliDetail(LoginRequiredMixin, View):

    def get(self, request):
        ret = dict()
        if 'id' in request.GET and request.GET['id']:
            detail = get_object_or_404(info, pk=request.GET.get('id'))
            details = info.objects.exclude(id=request.GET.get('id'))
            ret['detail'] = detail

        else:
            details = info.objects.all()
        ret['details'] = details
        return render(request, 'new/xiangmuguanli_detail.html', ret)

    def post(self, request):
        res = dict(result=False)
        user_id = request.POST.get("id")
        if request.method == "POST":
            username = request.POST.get("name")
            age = request.POST.get("age")
            address = request.POST.get("addr")
            models.info.objects.filter(id=user_id).update(name=username, age=age, addr=address)
            res['result'] = True
            return HttpResponse(json.dumps(res), content_type="application/json")

        return HttpResponse(json.dumps(res), content_type="application/json")


# 项目管理-用户信息-删除
class xiangmuGuanliDelete(LoginRequiredMixin, View):

    def post(self, request):
        res = dict(result=False)
        if "id" in request.POST and request.POST['id']:
            id_list = map(int, request.POST.get("id").split(','))
            models.info.objects.filter(id__in=id_list).delete()
            res['result'] = True

        return HttpResponse(json.dumps(res), content_type="application/json")


# 项目管理-用户信息-添加用户
class xiangmuGuanliAdd(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'new/xiangmuguanliadd_users.html')

    def post(self, request):
        res = dict(result=False)
        if request.method == "POST":
            id = request.POST.get("id")
            name = request.POST.get("name")
            age = request.POST.get("age")
            addr = request.POST.get("addr")

            models.info.objects.create(id=id, name=name, age=age, addr=addr)

            res['result'] = True

        return HttpResponse(json.dumps(res), content_type="application/json")
