#!/usr/bin/python3
"""
    This module defines
    a class City
    to manipulate instances
    and create and destroy
    """
from models.base_model import BaseModel


class City(BaseModel):
    """
    This class defines a City
        by various attributes
        """
    state_id = ""
    name = ""
