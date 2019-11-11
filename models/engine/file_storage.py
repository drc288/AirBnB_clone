#!/usr/bin/python3

import os.path
import json
"""
FileStorage - save file and get the data, save the data in
format JSON and create new object to save a json
"""


class FileStorage():
    """ FileStorage """
    def __init__(self):
        """
        __init__ init the constructor
        """
        self.__file_path = "file.json"
        # Create a EMPTY object
        self.__objects = dict()

    def all(self):
        """
        all - return the dict of the object
        """
        return self.__objects

    def new(self, obj):
        """
        new - set a __object attribute
        """
        # Enter to object ["id"] and put in id_c
        id_c = obj["id"]
        # Enter to object ["__class__"] and put in nameClass
        nameClass = obj["__class__"]
        # Create a new variable and construct the data
        key = nameClass + "." + id_c
        # Set the dict of __objects
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, "w", encoding="utf-8") as f:
            f.write(json.dumps(self.__objects))

    def reload(self):
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                data = f.read()
                self.__objects = json.loads(data)
        except FileNotFoundError:
            pass
