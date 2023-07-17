#!/usr/bin/python3
"""The `review` module defines a `Review` class
that inherits from `BaseModel`."""


from models.base_model import BaseModel


class Review(BaseModel):
    """Defines a class `Review` that inherits from `BaseModel `."""
    place_id = ""
    user_id = ""
    text = ""
