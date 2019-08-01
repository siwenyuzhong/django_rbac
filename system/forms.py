import re

from django import forms
from .models import SystemSetup


class SystemSetupForm(forms.ModelForm):
    class Meta:
        model = SystemSetup
        fields = '__all__'
