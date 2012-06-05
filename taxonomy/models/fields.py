# -*- coding: utf-8 -*-
'''
Created on 29.06.2011

@author: gorodechnyj
'''
from django.db import models
from django.utils import simplejson
from django.core.serializers.json import DjangoJSONEncoder

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
    
class JSONField(models.TextField):
    """JSONField is a generic textfield that neatly serializes/unserializes
    JSON objects seamlessly"""

    # Used so to_python() is called
    __metaclass__ = models.SubfieldBase

    def to_python(self, value):
        """Convert our string value to JSON after we load it from the DB"""

        if value == "":
            return None

        try:
            if isinstance(value, basestring):
                return simplejson.loads(value)
        except ValueError:
            pass

        return value

    def get_db_prep_save(self, value, connection):
        """Convert our JSON object to a string before we save"""

        if value == "":
            return None

        if isinstance(value, dict):
            value = simplejson.dumps(value, cls=DjangoJSONEncoder)

        return super(JSONField, self).get_db_prep_save(value, connection)     