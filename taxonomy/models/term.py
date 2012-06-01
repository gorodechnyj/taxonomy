# -*- coding: utf-8 -*-
'''
Created on 31.05.2012

@author: gorodechnyj
'''
from django.db import models
from .vocabulary import Vocabulary
from .materializedpath import MaterializedPath 

class Term(MaterializedPath):
    """Terms are associated with a specific Taxonomy, and should be generically usable with any contenttype"""
    vocabulary = models.ForeignKey(Vocabulary, related_name='terms')
    name = models.CharField(max_length=50)
    class Meta:
        app_label='taxonomy'

    def __unicode__(self):
        return self.name
    