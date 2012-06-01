# -*- coding: utf-8 -*-
'''
Created on 29.06.2011

@author: gorodechnyj
'''
from django.db import models

class IntegerListField(models.TextField):
    ''' This fields is used to store list of integer values. 
        Can be used to store list of table id's current instance is referenced from.     
    '''
    description = """Stores list of integer values. Serialises to comma separated string."""

    __metaclass__ = models.SubfieldBase    
    
    def to_python(self, _record):
        if _record is None:
            return []
        elif _record == "":
            return []
        elif isinstance(_record, basestring):
            _list = [int(item) for item in _record.split(',')]
            return _list
        if isinstance(_record, list):
            return _record
        else:
            return []
        
    def get_prep_value(self, _list):
        if not _list:
            return ""
        elif isinstance(_list, basestring):
            return _list
        else:
            return ','.join([str(item) for item in _list])
    
    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_prep_value(value)     