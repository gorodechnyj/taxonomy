# -*- coding: utf-8 -*-
'''
Created on 14.05.2012

@author: gorodechnyj
'''

from django.contrib.gis.db import models
from .fields import IntegerListField 

class MaterializedPath(models.Model):
    parent = models.ForeignKey('self', null=True, blank=True, default=None)
    path = IntegerListField(null=True, blank=True, default=None)
    level = models.IntegerField(null=True, blank=True, default=None)
    
    class Meta:
        abstract=True
