#!/usr/bin/python3

from datetime import datetime
from uuid import uuid4

"""
BaseModel - create the base object
"""

class BaseModel():
    """ BaseModel """
    def __init__(self, name = "", my_number = 0):
        self.name = name
        self.my_number = my_number
        self.id = str(uuid4())
        self.create_at = datetime.now()
        self.update_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.update_at = datetime.now()
