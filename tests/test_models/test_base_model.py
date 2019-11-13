#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
"""
TestBaseModel - Unittest for base_model
"""


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.objects = BaseModel()

    def test_instance(self):
        """Test if the instance is BaseModel"""
        self.assertIsInstance(self.objects, BaseModel)

    def test_docString_class(self):
        """
        Test docstring in class
        """
        self.assertIsNotNone(BaseModel.__doc__)

    def id_str(self):
        """Test if the id is a string """
        self.assertIsIntance(type(self.objects.id), str)

    def add_attribute(self):
        """
        Test to add the name and my_number attributes to the class
        """
        self.name = "Holberton"
        self.my_number = 89
        self.assertIsInstances(self.name, self.objects)
        self.assertIsInstances(self.my_number, self.objects)

if __name__ == '__main__':
    unittest.main()

