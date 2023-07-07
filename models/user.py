#!/usr/bin/python3
"""  nueva clase user
"""


from .base_model import BaseModel


class User(BaseModel):
    """objeto para crear la clase
    user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
