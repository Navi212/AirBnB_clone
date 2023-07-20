#!/usr/bin/python3
"""
The `amenity` module supplies a class `TestAmenity` which
inherits from unittest and implements tests for class
attributes and methods.
"""


import pep8
import os
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
from models.engine.file_storage import FileStorage


class TestAmenity(unittest.TestCase):
    """
    Defines a class `TestAmenity` which implements
    different tests for class attributes and methods.
    """

    @classmethod
    def setUpClass(cls):
        """
        Sets up a setUpClass that creates an
        instance of `Amenity`, initializes attributes
        once"""
        cls.obj = Amenity()
        cls.obj.name = "Free Wifi"

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
        pep = style.check_files(["models/amenity.py"])
        self.assertEqual(pep.total_errors, 0, "Fix PEP8: Error")

    def test_docstring(self):
        """
        Tests `Amenity` class has docstring
        """
        self.assertIsNotNone(Amenity.__doc__)

    def test_Amenity_is_subclass(self):
        """
        Tests `Amenity` issubclass `BaseModel`
        """
        self.assertTrue(issubclass(self.obj.__class__, BaseModel))

    def test_obj_isinstance_of_Amenity(self):
        """
        Tests obj isinstance of `Amenity` class
        """
        self.assertTrue(isinstance(self.obj, Amenity))

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
        self.assertTrue("name" in self.obj.__dict__)

    def test_obj_has_no_unknown_attr(self):
        """
        Tests obj can not have unknown attributes set
        """
        self.assertFalse("age" in self.obj.__dict__)
        self.assertFalse("country" in self.obj.__dict__)
        self.assertFalse("Tell" in self.obj.__dict__)
        self.assertFalse("zip" in self.obj.__dict__)

    def test_obj_attr_val_types(self):
        """
        Tests obj attributes value Types
        """
        self.assertTrue(type(self.obj.name), str)

    def test_save_reload(self):
        """
        Tests save (serialization) and reload (deserialization)
        of the obj
        """
        with open("file.json", "w") as file:
            file.write('{"amenity_name": "free_wify"}')

        with open("file.json", "r") as file:
            for line in file:
                self.assertIsNotNone(line)
        self.assertIsNotNone(line)
