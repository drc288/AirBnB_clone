#!/usr/bin/python3

import json
import models
"""
FileStorage - save file and get the data, save the data in
format JSON and create new object to save a json
"""


class FileStorage:
    """ FileStorage """
    def __init__(self):
        """
        __init__ init the constructor
        """
        self.__file_path = "file.json"
        # Create a EMPTY object other way
        # to create a empty dict is = {}
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
        id_c = obj.id
        # Enter to object ["__class__"] and put in nameClass
        # type[obj].__name__
        nameClass = type(obj).__name__
        # Create a new variable and construct the data
        key = str(nameClass) + "." + str(id_c)
        # Set the dict of __objects
        self.__objects[key] = obj

    def save(self):
        """
        save - save the file in __file_path
        """
        # Create new dict to add data
        # It is necessary since the obj is not
        # seralized for JSON
        new_dict = dict()
        for key, value in self.__objects.items():
            # To fix, how i import to_dict
            obj_dict = value.to_dict()
            new_dict[key] = obj_dict
        new_json = json.dumps(new_dict)
        with open(self.__file_path, "w", encoding="utf-8") as f:
            f.write(new_json)

    def reload(self):
        """
        reload - reload the data to json
        """
        try:
            with open(self.__file_path, encoding="utf-8") as f:
                data = f.read()
                self.__objects = json.loads(data)
        except:
            # if error pass
            pass
