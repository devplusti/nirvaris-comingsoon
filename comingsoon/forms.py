from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import KeepInTouchEmail

class KeepInTouchEmailForm(forms.ModelForm):

    anti_spam_token = forms.CharField(widget=forms.HiddenInput())
    anti_spam_hidden = forms.CharField(widget=forms.HiddenInput())
    anti_spam_no_hidden = forms.CharField(required=False,label='')

    class Meta:
        model = KeepInTouchEmail
        fields = [
            'email'
        ]

    def anti_spam(self):

        spam_token = uuid.uuid4()

        self.initial['anti_spam_token'] = str(spam_token)
        self.initial['anti_spam_no_hidden'] = str(spam_token)
        self.initial['anti_spam_hidden'] = ''