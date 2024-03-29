# -*- coding: utf-8 -*-
'''
Created on 31.05.2012

@author: gorodechnyj
'''
from django.db import models

class Vocabulary(models.Model):
    """A facility for creating custom content classification types""" 
    machine_name = models.CharField(max_length=50, unique=True)
    verbose_name = models.CharField(max_length=1024, unique=True)
    description = models.TextField(null=True)
    
    class Meta:
        verbose_name = "vocabulary"  
        verbose_name_plural = "vocabularies"
        app_label='taxonomy'        
    
    def __unicode__(self): 
        return self.name