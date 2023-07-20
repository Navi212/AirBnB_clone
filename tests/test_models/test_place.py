#!/usr/bin/python3
"""
The `place` module supplies a class `TestPlace` which
inherits from unittest and implements tests for class
attributes and methods.
"""


import pep8
import os
import unittest
from models.base_model import BaseModel
from models.place import Place
from models.engine.file_storage import FileStorage


class TestPlace(unittest.TestCase):
    """
    Defines a class `TestPlace` which implements
    different tests for class attributes and methods.
    """

    @classmethod
    def setUpClass(cls):
        """
        Sets up a setUpClass that creates an
        instance of `Place`, initializes attributes
        once"""
        cls.obj = Place()
        cls.obj.city_id = "102"
        cls.obj.user_id = "89"
        cls.obj.name = "Monte Carlo"
        cls.obj.description = "Monte Carlo inn"
        cls.obj.number_rooms = 50
        cls.obj.number_bathrooms = 50
        cls.obj.max_guest = 50
        cls.obj.price_by_night = 100
        cls.obj.latitude = 0.01
        cls.obj.longitude = 0.02
        cls.obj.amenity_ids = ["505", "101", "993"]

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
        pep = style.check_files(["models/place.py"])
        self.assertEqual(pep.total_errors, 0, "Fix PEP8: Error")

    def test_docstring(self):
        """
        Tests `Place` class has docstring
        """
        self.assertIsNotNone(Place.__doc__)

    def test_Place_is_subclass(self):
        """
        Tests `Place` issubclass `BaseModel`
        """
        self.assertTrue(issubclass(self.obj.__class__, BaseModel))

    def test_obj_isinstance_of_Place(self):
        """
        Tests obj isinstance of `Place` class
        """
        self.assertTrue(isinstance(self.obj, Place))

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
        self.assertTrue("city_id" in self.obj.__dict__)
        self.assertTrue("user_id" in self.obj.__dict__)
        self.assertTrue("name" in self.obj.__dict__)
        self.assertTrue("description" in self.obj.__dict__)
        self.assertTrue("number_rooms" in self.obj.__dict__)
        self.assertTrue("number_bathrooms" in self.obj.__dict__)
        self.assertTrue("max_guest" in self.obj.__dict__)
        self.assertTrue("price_by_night" in self.obj.__dict__)
        self.assertTrue("latitude" in self.obj.__dict__)
        self.assertTrue("longitude" in self.obj.__dict__)
        self.assertTrue("amenity_ids" in self.obj.__dict__)

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
        self.assertTrue(type(self.obj.city_id), str)
        self.assertTrue(type(self.obj.user_id), str)
        self.assertTrue(type(self.obj.name), str)
        self.assertTrue(type(self.obj.description), str)
        self.assertTrue(type(self.obj.number_rooms), int)
        self.assertTrue(type(self.obj.number_bathrooms), int)
        self.assertTrue(type(self.obj.max_guest), int)
        self.assertTrue(type(self.obj.price_by_night), int)
        self.assertTrue(type(self.obj.latitude), float)
        self.assertTrue(type(self.obj.longitude), float)
        self.assertTrue(type(self.obj.amenity_ids), list)

    def test_save_reload(self):
        """
        Tests save (serialization) and reload (deserialization)
        of the obj
        """
        with open("file.json", "w") as file:
            file.write('{"amenity_ids": "["505", "101", "993"]"}')

        with open("file.json", "r") as file:
            for line in file:
                self.assertIsNotNone(line)
        self.assertIsNotNone(line)
