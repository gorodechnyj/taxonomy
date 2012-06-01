# -*- coding: utf-8 -*-
'''
Created on 31.05.2012

@author: gorodechnyj
'''
from django.db import models
from .term import Term

class TermFeatures(models.Model):
    """Excessive storage for term features """
    term = models.OneToOneField(Term, related_name='features')
    name = models.CharField(max_length=1024)
    description = models.TextField(null = True, blank=True, default=None)
    icon = models.ImageField(upload_to='term/icons', verbose_name=u"Иконка товара", null=True, blank=True, default=None)
    unit = models.CharField(max_length=30, null=True, blank=True, default=None)
    key = models.CharField(max_length=1024, null=True, blank=True, default=None)
    value = models.FloatField(null=True, blank=True, default=None)
    class Meta:
        app_label='taxonomy'
        
    def __unicode__(self):
        return self.name