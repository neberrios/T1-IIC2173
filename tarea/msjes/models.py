# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Message(models.Model):
    message_text = models.CharField(max_length=150)
    pub_date = models.DateTimeField('date published')
    client_ip = models.CharField(max_length=150)
