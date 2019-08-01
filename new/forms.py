from django.forms import ModelForm

from new.models import info


class NewUpdateForm(ModelForm):
    class Meta:
        model = info
        fields = "__all__"
