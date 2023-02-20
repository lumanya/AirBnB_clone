#!/usr/bin/env python3
"""
 amenity module contain Amenity class that inherit from BaseModel
 with Public class attributes name
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Amenity class inherit from BaseModel
      Attributes:
        name (str): name of state
    """
    name = ""
