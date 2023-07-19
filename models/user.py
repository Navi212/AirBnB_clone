#!/usr/bin/python3
"""The `user` module supplies a class `User`
that inherits from `BaseModel`."""


from models.base_model import BaseModel


class User(BaseModel):
    """Defines a class `User` that inherits from `BaseModel`."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
