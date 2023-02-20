#!/usr/bin/env python3
"""
 place module contain Place class that inherit from BaseModel
 with Public class attributes
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """ Place class inherit from BaseModel
      Attributes:
        name (str): name of place
        city_id (str): city id
        user_id (str)_: user id
        description (str): description of a place
        number_rooms (int): nummber of rooms
        number_bathrooms (int): number of bathroooms
        max_guest (int): number of guest
        price_by_ningt (str): prce by ninght
        latitude (float): number of latitude
        amenity_ids:amenity id
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
