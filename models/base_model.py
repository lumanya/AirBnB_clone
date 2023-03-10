#!/usr/bin/python3
"""
 base_model is the module that contains BaseModel class
 BaseModel class is the base class in which all other class will inherit from
 this class
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
     BaseModel is the class in which all other cas inherit from this

     Methods:
      __str__(self)
      to_dict(self)
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize instance of the class

        Args:
        id (str): string-assign with an uuid when an instance is created
        created_at (str): datetime-assign with the current datetime when an
                         an instance is created
        updated_at (str): datetime-assign with the current datetime when an
                          an instance is created and is updated every time
                         we change our obejcts
        **kwargs (dict): contains attributs that create new instance
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.fromisoformat(value))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ print [<class name>] (<self.id>) <self.__dict__ of instance """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """
           updates the public instance attributes  updated_at
           with the current date time
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
         returns d dict values containg all keys/values of __dict__ of the
         instance
`        """
        dict = self.__dict__.copy()
        dict['__class__'] = self.__class__.__name__
        dict['created_at'] = self.created_at.isoformat()
        dict['updated_at'] = self.updated_at.isoformat()
        return dict
