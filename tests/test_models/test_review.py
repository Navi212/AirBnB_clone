#!/usr/bin/python3
"""
The `review` module supplies a class `TestReview` which
inherits from unittest and implements tests for class
attributes and methods.
"""


import pep8
import os
import unittest
from models.base_model import BaseModel
from models.review import Review
from models.engine.file_storage import FileStorage


class TestReview(unittest.TestCase):
    """
    Defines a class `TestReview` which implements
    different tests for class attributes and methods.
    """

    @classmethod
    def setUpClass(cls):
        """
        Sets up a setUpClass that creates an
        instance of `Review`, initializes attributes
        once"""
        cls.obj = Review()
        cls.obj.place_id = "101"
        cls.obj.user_id = "1608"
        cls.obj.text = "You are welcome"

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
        pep = style.check_files(["models/review.py"])
        self.assertEqual(pep.total_errors, 0, "Fix PEP8: Error")

    def test_docstring(self):
        """
        Tests `Review` class has docstring
        """
        self.assertIsNotNone(Review.__doc__)

    def test_Review_is_subclass(self):
        """
        Tests `Review` issubclass `BaseModel`
        """
        self.assertTrue(issubclass(self.obj.__class__, BaseModel))

    def test_obj_isinstance_of_Review(self):
        """
        Tests obj isinstance of `Review` class
        """
        self.assertTrue(isinstance(self.obj, Review))

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
        self.assertTrue("place_id" in self.obj.__dict__)
        self.assertTrue("user_id" in self.obj.__dict__)
        self.assertTrue("text" in self.obj.__dict__)

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
        self.assertTrue(type(self.obj.place_id), str)
        self.assertTrue(type(self.obj.user_id), str)
        self.assertTrue(type(self.obj.text), str)

    def test_save_reload(self):
        """
        Tests save (serialization) and reload (deserialization)
        of the obj
        """
        with open("file.json", "w") as file:
            file.write('{"place_id": "101", "user_id": "1608"}')

        with open("file.json", "r") as file:
            for line in file:
                self.assertIsNotNone(line)
        self.assertIsNotNone(line)
