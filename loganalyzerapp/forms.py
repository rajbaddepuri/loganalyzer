from .models import log,log_fields
from django import forms


class log_form(forms.ModelForm):
    class Meta:
        fields='__all__'
        model=log
