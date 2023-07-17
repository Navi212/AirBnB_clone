#!/usr/bin/python3
"""
The `amenity` mdule supplies an `Amenity` class
that inherits from `BaseModel`.
"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """Defines `Amenity` class"""
    name = ""
