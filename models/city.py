#!/usr/bin/env python3
"""
 city module that contains City class that inherit from BaseModel class
 with public instance name
"""
from models.base_model import BaseModel


class City(BaseModel):
    """ City class inherit from BaseModel

    Attributes:
      state_id (str): empty string
      name (str): empty string
    """
    state_id = ""
    name = ""
