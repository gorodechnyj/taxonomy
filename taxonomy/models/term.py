# -*- coding: utf-8 -*-
'''
Created on 31.05.2012

@author: gorodechnyj
'''
from django.db import models
from source.models import Source
from .vocabulary import Vocabulary
from .materializedpath import MaterializedPath
from .fields import JSONField 

class Term(MaterializedPath):
    """Terms are associated with a specific Taxonomy, and should be generically usable with any contenttype"""
    source = models.ForeignKey(Source, related_name="external_%(class)s_set", default=None)    
    source_code = models.CharField('Key value of source object in external database', max_length=128, default=None)
    vocabulary = models.ForeignKey(Vocabulary, related_name='terms')
    name = models.CharField(max_length=1024)
    short_name = models.CharField(max_length=50, null=True, blank=True, default=None)
    weight = models.IntegerField(verbose_name=u'Вес сортировки', null=True, blank=True, default=0)
    icon = models.ImageField(upload_to='term/icons', verbose_name=u"Иконка товара", null=True, blank=True, default=None)
    metadata = JSONField(null=True, blank=True, default=None)
    class Meta:
        app_label='taxonomy'

    def __unicode__(self):
        return self.name
    