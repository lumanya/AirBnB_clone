#!/usr/bin/env python3
"""
 review is the module that contains class Review which inherite from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class that inherits from BaseModel
    attributes:
    place_id (str): place id
    user_id (str): user_id
    text (str): text
    """

    place_id = ""
    user_id = ""
    text = ""
