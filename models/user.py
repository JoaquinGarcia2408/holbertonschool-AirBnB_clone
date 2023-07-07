#!/usr/bin/python3
"""  nueva clase user
"""


from .base_model import BaseModel


class User(BaseModel):
    """objeto para crear la clase
    user
    """
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""

