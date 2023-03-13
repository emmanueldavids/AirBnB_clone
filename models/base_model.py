#!/usr/bin/python3

import uuid
import sys
import datetime


class BaseModel:
    # Initializing a method for the base class
    def __init__(self, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
    
    def __str__(self):
        # converts the BaseModel into a string
        cls_name = type(self).__name__
        return f"[{cls_name}]{self.id} {self.created_at}]"
    
    def save(self):
        # saves the updated datetime
        self.updated_at = datetime.datetime.now()
        
    def to_dict(self):
        # converting the attributes to a dictionary
        base_dict = self.__dict__
        base_dict['__class__'] = self.__class__.__name__
        base_dict['created_at'] = self.created_at
        base_dict['updated_at'] = self.updated_at
        return base_dict

  