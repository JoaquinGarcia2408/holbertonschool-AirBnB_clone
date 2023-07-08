#!/usr/bin/python3
""" review """
from .base_model import BaseModel


class Review(BaseModel):
    """
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    place_id = ''
    user_id = ''
    text = ''
