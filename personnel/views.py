from django.shortcuts import render
from django.views.generic.base import View

from utils.mixin_utils import LoginRequiredMixin
from rbac.models import Menu
from system.models import SystemSetup

class PersonnelView(LoginRequiredMixin,View):

    def get(self,request):
        return render(request,'personnel/personnel_index.html')
