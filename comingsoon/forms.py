from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import KeepInTouchEmail

class KeepInTouchEmailForm(forms.ModelForm):
    class Meta:
        model = KeepInTouchEmail
        fields = [
            'email'
        ]