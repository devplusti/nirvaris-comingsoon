import pdb,sys

from threading import Thread

from django.contrib import messages
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext as _
from django.views.generic import TemplateView
from django.views.generic.base import View
# Create your views here.

from .email import send_keep_in_touch_email
from .forms import KeepInTouchEmailForm
from .models import KeepInTouchEmail

class KeepInTouchEmailView(View):
    template_name = "coming-soon-keep-in-touch-email.html"

    def get(self, request):
        form = KeepInTouchEmailForm()

        request_context = RequestContext(request,{'form':form})

        return render_to_response(self.template_name, request_context)

    def post(self, request):
        form = KeepInTouchEmailForm(request.POST)

        form_valid = form.is_valid()
        cleaned_data = form.clean()

        if form_valid:

            try:
                form.save()
                thread = Thread(target=send_keep_in_touch_email, args=(cleaned_data['email'],))
                thread.start()
                form = KeepInTouchEmailForm()
                messages.success(self.request,_("Thank you!! We will keep in touch!"))
            except:
                #pdb.set_trace()
                messages.error(self.request,_('Sorry! We could not check your email.'))

        request_context = RequestContext(request,{'form':form})

        return render_to_response(self.template_name, request_context)