#!/usr/bin/python3
"""The `test_base_model` supplies a class `TestBaseModel_init_method
that inherits from `unittest` which implements a test class
with methods for our class attributes (methods)."""


import unittest
from models.base_model import BaseModel
from datetime import datetime
from models import storage


class TestBaseModel_init_method(unittest.TestCase):
    """Defines `TestBaseModel_methods` class
    for our class attributes (methods)."""

    def setUp(self):
        """Creates an instance of `BaseModel` for testings"""
        self.obj_1 = BaseModel()
        self.obj_2 = BaseModel()

    def tearDown(self):
        """Deletes the created object"""
        del self.obj_1
        del self.obj_2

    def test_init_id_str_type(self):
        """Tests type(id) is str"""
        self.assertTrue(type(self.obj_1.id), str)

    def test_obj_is_type_basemodel(self):
        """Tests obj is instance of `BaseModel`"""
        self.assertTrue(BaseModel, type(BaseModel()))

    def test_created_at_time_obj(self):
        """Tests the created_at during instantiation is a
        datetime object"""
        self.assertTrue(type(self.obj_1.created_at), datetime)

    def test_updated_at_time_obj(self):
        """Tests the updated_at during instantiation is a
        datetime object"""
        self.assertTrue(type(self.obj_1.updated_at), datetime)

    def test_uniq_id(self):
        """Tests id's for different objs are unique"""
        self.assertNotEqual(self.obj_1.id, self.obj_2.id)

    def test_creation_times_are_different(self):
        """Tests time difference for objects created similar time"""
        self.assertNotEqual(self.obj_1.created_at, self.obj_2.created_at)


class TestBaseModel_str_method(unittest.TestCase):
    """Defines a class `TestBaseModel_str_method` which
    tests the __str__ method of `BaseModel` class."""

    def test_str_return_type(self):
        """Tests the return type of __str__ method"""
        obj_1 = BaseModel()
        self.assertTrue(type(obj_1.__str__()), str)


class TestBaseModel_save_method(unittest.TestCase):
    """Defines a class `TestBaseModel_save_method` which
    tests the save method of the `BaseModel` class."""

    def test_save_updated_time_difference(self):
        """Tests update_at time difference between
        obj first creation time and update_at time
        after calling the save method"""
        obj_1 = BaseModel()
        first_udated_t = obj_1.updated_at
        storage.save()
        obj_1 = BaseModel()
        second_updated_t = obj_1.updated_at
        self.assertNotEqual(first_udated_t, second_updated_t)

    def test_args_unused(self):
        """Tests None is not stored"""
        obj_1 = BaseModel()
        self.assertNotIn(None, obj_1.__dict__.values())


class TestBaseModel_to_dict_method(unittest.TestCase):
    """Defines a class `TestBaseModel_to_dict_method` which
    tests the to_dict method of the `BaseModel` class."""

    def test_to_dict_values_are_set(self):
        """Tests to_dict return type is dict"""
        obj_1 = BaseModel()
        self.assertTrue(type(obj_1.to_dict()), dict)

    def test_to_dict_contains_correct_keys(self):
        """Tests to_dict contains the correct keys"""
        obj_1 = BaseModel()
        self.assertIn("__class__", obj_1.to_dict())
        self.assertIn("id", obj_1.to_dict())
        self.assertIn("created_at", obj_1.to_dict())
        self.assertIn("updated_at", obj_1.to_dict())

    def test_to_dict_equal_to_dunder(self):
        """Tests to_dict contains same attributes
        of an instance as the __dict__ (dunder method)"""
        obj_1 = BaseModel()
        self.assertEqual(obj_1.__dict__, obj_1.to_dict())

    def test_to_dict_contains_attr_set(self):
        """Tests attr contains values set"""
        obj_1 = BaseModel()
        obj_1.name = "ALX"
        obj_1.age = 100
        self.assertIn("name", obj_1.to_dict())
        self.assertIn("age", obj_1.to_dict())

    def test_to_dict_return_dict(self):
        """Tests to_dict return type (dict)"""
        obj_1 = BaseModel()
        self.assertEqual(dict, type(obj_1.to_dict()))

    def test_dict_output(self):
        """Tests dict output"""
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

    def test_to_dict_none_arg_error(self):
        """Tests to_dict raise TypeError on None
        type or non dict type arg"""
        obj_1 = BaseModel()
        with self.assertRaises(TypeError):
            obj_1.to_dict(None)
        with self.assertRaises(TypeError):
            obj_1.to_dict(1)
        with self.assertRaises(TypeError):
            obj_1.to_dict(12.12)
        with self.assertRaises(TypeError):
            obj_1.to_dict(["12", 11, (1, 2)])
        with self.assertRaises(TypeError):
            obj_1.to_dict((12, 33))
        with self.assertRaises(TypeError):
            obj_1.to_dict("str")


if __name__ == "__main__":
    unittest.main()
