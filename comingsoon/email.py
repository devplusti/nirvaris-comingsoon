import pdb
import logging
from datetime import date

from django.conf import settings
from django.core.mail.message import EmailMessage
from django.template.loader import render_to_string


def send_keep_in_touch_email( email):

    #pdb.set_trace()

    dic_for_context = {}
    dic_for_context['email'] = email
    dic_for_context['product_name'] = settings.NV_THEME_TITLE
    dic_for_context['site_url'] = settings.NV_SITE_URL

    subject = render_to_string('email-subject-keep-in-touch.txt', dic_for_context)
    template = render_to_string('email-body-keep-in-touch.html', dic_for_context)

    msg = EmailMessage(subject, template, settings.NV_EMAIL_FROM, [settings.NV_SEND_TO])

    msg.content_subtype = "html"
    msg.send()

