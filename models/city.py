#!/usr/bin/python3
"""This module creates a City User class"""

from models.base_model import BaseModel


class City(BaseModel):
    """The Class for managing city objects"""

    state_id = ""
    name = ""
