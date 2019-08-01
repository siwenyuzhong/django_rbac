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


class NewView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'new/xiangmuguanli.html')
