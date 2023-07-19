#!/usr/bin/python3
"""
The `base_module` module defines a base class for
other derived classes.
"""


import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Defines `BaseModel` class which represents a parent class
    for other classes."""
    def __init__(self, *args, **kwargs):
        if kwargs:
            fm = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key in {"created_at", "updated_at"}:
                    kwargs[key] = datetime.strptime(value, fm)
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Returns an informal string representation of an object."""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """Updates the public instance attribute updated_at
        with the current datetime."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of an instance(objects)
        containing all keys/values of __dict__ of an instance(object)."""
        fm = "%Y-%m-%dT%H:%M:%S.%f"
        obj_dict = self.__dict__
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = datetime.now().strftime(fm)
        obj_dict["updated_at"] = datetime.now().strftime(fm)
        return (obj_dict)
