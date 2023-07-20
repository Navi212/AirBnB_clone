#!/usr/bin/python3
"""
The `base_model` module supplies a class `TestBaseModel` which
inherits from unittest and implements tests for class
attributes and methods.
"""


import pep8
import os
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from datetime import datetime
from time import sleep


class TestBaseModel_init_method(unittest.TestCase):
    """
    Defines `TestBaseModel_methods` class
    for our class attributes (methods).
    """

    @classmethod
    def setUpClass(cls):
        """
        Sets up a setUpClass that creates an
        instance of `BaseModel, initializes attributes
        once"""
        cls.obj_1 = BaseModel()
        sleep(0.10)
        cls.obj_2 = BaseModel()

    @classmethod
    def tearDownClass(cls):
        """
        Sets a tearDownClass that performs a cleanup
        after all operations are completed
        """
        del cls.obj_1
        del cls.obj_2
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_pep8(self):
        """
        Tests conformance to pep8
        """
        style = pep8.StyleGuide(quiet=True)
        pep = style.check_files(["models/base_model.py"])
        self.assertEqual(pep.total_errors, 0, "Fix PEP8: Error")

    def test_docstring(self):
        """
        Tests `BaseModel` class has docstring
        """
        self.assertIsNotNone(BaseModel.__doc__)

    def test_init_id_attr_types(self):
        """
        Tests instance attribute types
        """
        self.assertTrue(type(self.obj_1.id), str)
        self.assertTrue(type(self.obj_2.id), str)
        self.assertTrue(type(self.obj_1.created_at), datetime)
        self.assertTrue(type(self.obj_2.created_at), datetime)
        self.assertTrue(type(self.obj_1.updated_at), datetime)
        self.assertTrue(type(self.obj_2.updated_at), datetime)

    def test_objs_isinstance_basemodel(self):
        """
        Tests obj_1 and obj_2 are instances of `BaseModel`
        """
        self.assertTrue(isinstance(self.obj_1, BaseModel))
        self.assertTrue(isinstance(self.obj_2, BaseModel))

    def test_unique_ids(self):
        """
        Tests id's are unique for each instance of a class
        """
        self.assertNotEqual(self.obj_1.id, self.obj_2.id)

    def test_attr_are_present(self):
        """
        Tests class attributes are present in instance __dict__
        """
        self.assertIn("id", self.obj_1.__dict__)
        self.assertIn("id", self.obj_2.__dict__)
        self.assertIn("created_at", self.obj_1.__dict__)
        self.assertIn("created_at", self.obj_2.__dict__)
        self.assertIn("updated_at", self.obj_1.__dict__)
        self.assertIn("updated_at", self.obj_2.__dict__)

    def test_instance_dict_not_None(self):
        """
        Tests instance dict is not None after instantiation
        """
        self.assertIsNotNone(self.obj_1.__dict__)
        self.assertIsNotNone(self.obj_2.__dict__)

    def test_creation_times_are_different(self):
        """
        Tests time difference for objects created similar time
        """
        self.assertNotEqual(self.obj_1.created_at, self.obj_2.created_at)


class TestBaseModel_str_method(unittest.TestCase):
    """
    Defines a class `TestBaseModel_str_method` which
    tests the __str__ method of `BaseModel` class.
    """
    def test_str_return_type(self):
        """
        Tests the return type of __str__ method
        """
        obj_1 = BaseModel()
        self.assertTrue(type(obj_1.__str__()), str)


class TestBaseModel_save_method(unittest.TestCase):
    """
    Defines a class `TestBaseModel_save_method` which
    tests the save method of the `BaseModel` class.
    """
    def test_save_updated_time_difference(self):
        """
        Tests update_at time difference between
        obj first creation time and update_at time
        after calling the save method
        """
        obj_1 = BaseModel()
        first_udated_t = obj_1.updated_at
        storage.save()
        obj_2 = BaseModel()
        second_updated_t = obj_2.updated_at
        self.assertNotEqual(first_udated_t, second_updated_t)

    def test_args_unused(self):
        """
        Tests None is not stored
        """
        obj_1 = BaseModel()
        self.assertNotIn(None, obj_1.__dict__.values())


class TestBaseModel_to_dict_method(unittest.TestCase):
    """
    Defines a class `TestBaseModel_to_dict_method` which
    tests the to_dict method of the `BaseModel` class.
    """

    def test_to_dict_values_are_set(self):
        """
        Tests to_dict return type is dict
        """
        obj_1 = BaseModel()
        self.assertTrue(type(obj_1.to_dict()), dict)

    def test_to_dict_contains_correct_keys(self):
        """
        Tests to_dict contains the correct keys
        """
        obj_1 = BaseModel()
        self.assertIn("__class__", obj_1.to_dict())
        self.assertIn("id", obj_1.to_dict())
        self.assertIn("created_at", obj_1.to_dict())
        self.assertIn("updated_at", obj_1.to_dict())

    def test_to_dict_equal_to_dunder(self):
        """
        Tests to_dict contains same attributes
        of an instance as the __dict__ (dunder method)
        """
        obj_1 = BaseModel()
        self.assertEqual(obj_1.__dict__, obj_1.to_dict())

    def test_to_dict_contains_attr_set(self):
        """
        Tests attr contains values set
        """
        obj_1 = BaseModel()
        obj_1.name = "ALX"
        obj_1.age = 100
        self.assertIn("name", obj_1.to_dict())
        self.assertIn("age", obj_1.to_dict())

    def test_to_dict_return_dict(self):
        """
        Tests to_dict return type (dict)
        """
        obj_1 = BaseModel()
        self.assertEqual(dict, type(obj_1.to_dict()))

    def test_dict_output(self):
        """
        Tests dict output
        """
        obj_1 = BaseModel()
        dtime = datetime.now()
        fm = "%Y-%m-%dT%H:%M:%S.%f"
        obj_1.id = "1010"
        obj_1.created_at = obj_1.updated_at = dtime
        to_dit_dict = {
            "id": "1010",
            "__class__": "BaseModel",
            "created_at": dtime.strftime(fm),
            "updated_at": dtime.strftime(fm)
        }
        self.assertTrue(to_dit_dict, obj_1.to_dict())


if __name__ == "__main__":
    unittest.main()
