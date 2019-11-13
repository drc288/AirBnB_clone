#!/usr/bin/python3
"""
TestUser - To prube the class user
"""

import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):

    def setUp(self):
        self.obj = User()

    def test_is_instance(self):
        self.assertIsInstance(self.obj, User)

    def test_user_inherits_basemodel(self):
        self.assertIsInstance(self.obj, BaseModel)
