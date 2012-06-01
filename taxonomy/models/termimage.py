# -*- coding: utf-8 -*-
'''
Created on 31.05.2012

@author: gorodechnyj
'''
from django.db import models
from .term import Term

class TermImage(models.Model):
    term = models.ForeignKey(Term, related_name='image')
    image = models.ImageField(upload_to='term/image', verbose_name=u"Изображение товара", null=True, blank=True, default=None)
    class Meta:
        app_label='taxonomy'    