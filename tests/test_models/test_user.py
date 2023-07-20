#!/usr/bin/python3
"""
The `user` module supplies a class `TestUser` which
inherits from unittest and implements tests for class
attributes and methods.
"""


import pep8
import os
import unittest
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage


class TestUser(unittest.TestCase):
    """
    Defines a class `TestUser` which implements
    different tests for class attributes and methods.
    """

    @classmethod
    def setUpClass(cls):
        """
        Sets up a setUpClass that creates an
        instance of `User`, initializes attributes
        once"""
        cls.obj = User()
        cls.obj.email = "nav1212@alxswe.com"
        cls.obj.password = "root"
        cls.obj.first_name = "Joe"
        cls.obj.last_name = "Navi"

    @classmethod
    def tearDownClass(cls):
        """
        Sets a tearDownClass that performs a cleanup
        after all operations are completed
        """
        del cls.obj
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_pep8(self):
        """
        Tests conformance to pep8
        """
        style = pep8.StyleGuide(quiet=True)
        pep = style.check_files(["models/user.py"])
        self.assertEqual(pep.total_errors, 0, "Fix PEP8: Error")

    def test_docstring(self):
        """
        Tests `User` class has docstring
        """
        self.assertIsNotNone(User.__doc__)

    def test_User_is_subclass(self):
        """
        Tests `User` issubclass `BaseModel`
        """
        self.assertTrue(issubclass(self.obj.__class__, BaseModel))

    def test_obj_isinstance_of_User(self):
        """
        Tests obj isinstance of `User` class
        """
        self.assertTrue(isinstance(self.obj, User))

    def test_obj_dict_not_empty(self):
        """
        Tests obj_dict is not empty after instantiation
        of the `FileStorage` class
        """
        storage = FileStorage()
        obj_dict = storage.all()
        self.assertIsNotNone(obj_dict)

    def test_obj_dict_is_dict(self):
        """
        Tests obj attributes set exists
        """
        storage = FileStorage()
        obj_dict = storage.all()
        self.assertTrue(type(obj_dict), dict)

    def test_obj_is_not_non(self):
        """
        Tests obj is not None
        """
        self.assertIsNotNone(self)

    def test_obj_has_attr(self):
        """
        Tests obj has attributes
        """
        self.assertTrue("email" in self.obj.__dict__)
        self.assertTrue("password" in self.obj.__dict__)
        self.assertTrue("first_name" in self.obj.__dict__)
        self.assertTrue("last_name" in self.obj.__dict__)

    def test_obj_has_no_unknown_attr(self):
        """
        Tests obj can not have unknown attributes set
        """
        self.assertFalse("age" in self.obj.__dict__)
        self.assertFalse("country" in self.obj.__dict__)
        self.assertFalse("state" in self.obj.__dict__)
        self.assertFalse("zip" in self.obj.__dict__)

    def test_obj_attr_val_types(self):
        """
        Tests obj attributes value Types
        """
        self.assertTrue(type(self.obj.email), str)
        self.assertTrue(type(self.obj.password), str)
        self.assertTrue(type(self.obj.first_name), str)
        self.assertTrue(type(self.obj.last_name), str)

    def test_save_reload(self):
        """
        Tests save (serialization) and reload (deserialization)
        of the obj
        """
        with open("file.json", "w") as file:
            file.write('{"first_name": "Navi", "last_name": "Joe"}')

        with open("file.json", "r") as file:
            for line in file:
                self.assertIsNotNone(line)
        self.assertIsNotNone(line)
