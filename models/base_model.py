#!/usr/bin/python3

from datetime import datetime
from uuid import uuid4
"""
BaseModel - create the base object
"""


class BaseModel():
    """ BaseModel """
    def __init__(self, *args, **kwargs):
        """
        __init__ construct the class, initialice the
         id, created at and updated at.
         kwargs - get a new dict and converte the data a
         BaseModel
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = kwargs['id']
                elif key == "created_at":
                    # Convert to string a datetime format, using
                    # datetime.strptime([date in str],
                    # ["the format of the string"])
                    self.created_at = datetime.strptime(kwargs['created_at'],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(kwargs['updated_at'],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    # Add others values, create in object the keys
                    # if not are id, updated_at
                    # and created_at, create the data using self.__dict__
                    self.__dict__[key] = value
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        __str__ return a example of the output.
        """
        return "[{}] ({}) {}".format(__class__.__name__,
                                     self.id, self.__dict__)

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
        # Create the isoformat for datetime.now()
        self.__dict__["created_at"] = self.created_at.isoformat()
        self.__dict__["updated_at"] = self.updated_at.isoformat()
        self.__dict__['__class__'] = __class__.__name__
        return self.__dict__
