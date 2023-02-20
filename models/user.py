#!/usr/bin/env python3
"""
 user is the module that contains class User which inherite from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class that inherits from BaseModel
    attributes:
    email (str): empyt string
    password (str): empty string
    first_name (str): empyt sting
    last_name (str): empty string
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
