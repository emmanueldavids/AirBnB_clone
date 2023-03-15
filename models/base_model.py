#!/usr/bin/python3
from queue import Empty
import models
import uuid
import sys
import datetime


class BaseModel:
    # Initializing a method for the base class
    def __init__(self, *args, **kwargs):

        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key != '__class__':
                     if key == 'created_at' or key == 'updated_at':
                        value = datetime.fromisoformat(value)
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        # converts the BaseModel into a string
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        # saves the updated datetime
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        # converting the attributes to a dictionary
        base_dict = self.__dict__
        base_dict['__class__'] = self.__class__.__name__
        base_dict['created_at'] = self.created_at.isoformat()
        base_dict['updated_at'] = self.updated_at.isoformat()
        return base_dict
