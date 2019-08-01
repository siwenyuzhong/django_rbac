from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from app01 import models
# Create your views here.
from django.views.generic.base import View
from utils.mixin_utils import LoginRequiredMixin
import json
from django.core.serializers.json import DjangoJSONEncoder
from system.models import SystemSetup
from rbac.models import Menu
from django.shortcuts import get_object_or_404
import datetime


# remote
class Remote(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'app01/remote.html')


# index
class RmoteConnectionInfo(LoginRequiredMixin, View):

    def get(self, request):
        osinfo_list = models.ServerInfos.objects.all()
        return render(request, 'app01/remote_center.html', locals())


# list api
class RmoteConnectionInfoList(LoginRequiredMixin, View):

    def get(self, request):
        fields = ['id', 'server_name', 'ip_addr', 'status', 'memo']
        filters = dict()
        osinfo_list = dict(data=list(models.ServerInfos.objects.filter(**filters).values(*fields)))
        return HttpResponse(json.dumps(osinfo_list, cls=DjangoJSONEncoder), content_type='application/json')


from .forms import App01UPdateForms
from app01.models import ServerInfos


# modify
class RmoteConnectionInfoDetail(LoginRequiredMixin, View):

    def get(self, request):
        ret = dict()
        if 'id' in request.GET and request.GET['id']:
            detail = get_object_or_404(ServerInfos, pk=request.GET.get('id'))
            details = ServerInfos.objects.exclude(id=request.GET.get('id'))
            ret['detail'] = detail

        else:
            details = ServerInfos.objects.all()
        ret['details'] = details
        return render(request, 'app01/RmoteConnectionInfoDetail.html', ret)

    # way 1
    # def post(self, request):
    #     res = dict(result=False)
    #     if 'id' in request.POST and request.POST['id']:
    #         structure = get_object_or_404(ServerInfos, pk=request.POST.get('id'))
    #     else:
    #         structure = ServerInfos()
    #
    #     structure_update_form = App01UPdateForms(request.POST, instance=structure)
    #     print(structure_update_form)
    #     if structure_update_form.is_valid():
    #         structure_update_form.save()
    #         res['result'] = True
    #
    #     return HttpResponse(json.dumps(res), content_type='application/json')

    # way 2 modelform
    # def post(self, request):
    #     res = dict(result=False)
    #     edit_user = models.ServerInfos.objects.filter(pk=request.POST.get("id")).first()
    #     if request.method == "POST":
    #         form = App01UPdateForms(request.POST, instance=edit_user)
    #         if form.is_valid():
    #             print(form.cleaned_data)
    #             form.save()
    #             res['result'] = True
    #
    #         return HttpResponse(json.dumps(res), content_type='application/json')
    #
    #     return HttpResponse(json.dumps(res), content_type='application/json')

    def post(self, request):
        res = dict(result=False)
        edit_id = request.POST.get("id")

        if request.method == "POST":
            server_name = request.POST.get("server_name")
            ip_addr = request.POST.get("ip_addr")
            port = request.POST.get("port")
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            username = request.POST.get("username")
            memo = request.POST.get("memo")

            models.ServerInfos.objects.filter(id=edit_id).update(server_name=server_name, ip_addr=ip_addr, port=port,
                                                                 username=username, datetime=now, memo=memo)
            res['result'] = True
        return HttpResponse(json.dumps(res), content_type="application/json")


# delete
class RmoteConnectionInfoDelete(LoginRequiredMixin, View):

    def post(self, request):
        res = dict(result=False)
        if request.method == "POST":
            rid = request.POST.get("id")
            models.ServerInfos.objects.filter(id=rid).delete()
            res['result'] = True
        return HttpResponse(json.dumps(res), content_type="application/json")


def tools(s):
    if s == "在线":
        return 1
    elif s == "宕机":
        return 2
    elif s == "网络不可达":
        return 3
    elif s == "下线":
        return 4


# add
class RmoteConnectionInfoAdd(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'app01/RmoteConnectionInfoAdd.html')

    def post(self, request):
        res = dict(result=False)
        if request.method == "POST":
            server_name = request.POST.get("server_name")
            ip_addr = request.POST.get("ip_addr")
            port = request.POST.get("port")
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            username = request.POST.get("username")
            memo = request.POST.get("memo")

            models.ServerInfos.objects.create(server_name=server_name, ip_addr=ip_addr, port=port, username=username,
                                              datetime=now, memo=memo)

            res['result'] = True

        return HttpResponse(json.dumps(res), content_type="application/json")
