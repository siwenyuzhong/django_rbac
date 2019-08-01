from app01.models import ServerInfos
from django.forms import ModelForm
from django import forms


class App01UPdateForms(ModelForm):
    class Meta:
        model = ServerInfos
        fields = ['server_name', 'status', 'ip_addr', 'memo','username','port','auth','datetime']

    # status字段必填导致更新失败，将此字段设置为非必填
    def __init__(self, *args, **kwargs):
        super(App01UPdateForms, self).__init__(*args, **kwargs)
        self.fields['status'].required = False
