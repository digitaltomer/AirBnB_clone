#!/usr/bin/python3
"""Module for Class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents a User"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
