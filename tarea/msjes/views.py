# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Message
from django.utils import timezone
from django.template import loader
from django.contrib import admin

##from .forms import CommentForm

def index(request):
    if request.method == 'POST':
        req = request.POST
        if req.get('comentario'):
            comentario = req.get('comentario')
            m = Message(message_text=comentario, pub_date=timezone.now(), client_ip= request.META['REMOTE_ADDR'])
            m.save()

    newest_messages_list = Message.objects.order_by('-pub_date')[:4]
    ##output = '\n'.join([m.message_text for m in newest_messages_list])
    template = loader.get_template('msjes/index.html')
    context = {'newest_messages_list': newest_messages_list}
    return render(request, 'msjes/index.html', context)

def comment(request):
    return render(request, 'msjes/comment.html')
