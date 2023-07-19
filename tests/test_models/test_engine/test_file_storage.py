#!/usr/bin/python3
"""The `test_file_storage` module supplies a class `TestFileStorage
that inherits from `unittest` and implements tests for all class
attributes and methods."""


import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Defines a class `TestFileStorage` that implements
    tests for class attributes and methods"""

    def test_doc_string(self):
        """Tests docstring"""
        self.assertIsNotNone(FileStorage.__doc__)

    def test_method_documentations(self):
        """Tests all methods of `FileStorage`
        has valid documentations"""
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_file_storage_working(self):
        """Tests `FileStorage` working properly"""
        obj = FileStorage()
        self.assertTrue(obj)
        self.assertIsNotNone(obj)
        self.assertTrue(type(obj), dict)

    def test_all_returns_dict(self):
        """Tests all returns a dict"""
        storage = FileStorage()
        obj = storage.all()
        self.assertTrue(type(obj), dict)


if __name__ == "__main__":
    unittest.main()
