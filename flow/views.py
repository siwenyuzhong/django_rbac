from django.shortcuts import render
from django.views.generic import View
from utils.mixin_utils import LoginRequiredMixin
from rbac.models import Menu
from system.models import SystemSetup


class FlowView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'flow/flow-index.html')
