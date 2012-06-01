# -*- coding: utf-8 -*-
'''
Created on 01.06.2012

@author: gorodechnyj
'''
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from .vocabulary import Vocabulary

class VocabularyRelation(models.Model):
    vocabulary = models.ForeignKey(Vocabulary)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    class Meta:
        app_label='taxonomy'    
