#!/usr/bin/python3

from datetime import datetime
from uuid import uuid4

"""
BaseModel - create the base object
"""

class BaseModel():
    """ BaseModel """
    def __init__(self):
        """
        __init__ construct the class, initialice the
         id, created at and updated at.
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        __str__ return a example of the output.
        """
        return "[{}] ({}) {}".format(__class__.__name__, self.id, self.__dict__)

    # Public instnace

    def save(self):
        """
        save - update the date of update_at.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        to_dict - return a string to a dict of the BaseModel.
        """
        self.__dict__["created_at"] = self.created_at.isoformat()
        self.__dict__["updated_at"] = self.updated_at.isoformat()
        self.__dict__['__class__'] = __class__.__name__
        return self.__dict__

