#!/usr/bin/python3
"""The `city` module supplies a class `City`
that inherits from `BaseModel`"""


from models.base_model import BaseModel


class City(BaseModel):
    """Defines a class `City` that inherits from `BaseModel`."""
    state_id = ""
    name = ""
