#!/usr/bin/python3
"""This module creates a Review User class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """This Class is  for managing review objects"""

    place_id = ""
    user_id = ""
    text = ""
