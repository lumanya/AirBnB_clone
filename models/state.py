#!/usr/bin/env python3
"""
 state module contain State class that inherit from BaseModel
 with Public class attributes name
"""
from models.base_model import BaseModel


class State(BaseModel):
    """ State class inherit from BaseModel
      Attributes:
        name (str): name of state
    """
    name = ""
