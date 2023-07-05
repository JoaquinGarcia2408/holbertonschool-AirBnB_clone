#!/usr/bin/python3
"""
    toda la data
"""

from uuid import uuid4
import datetime


class BaseModel:
    """sumary_line
       Keyword arguments:
       argument -- description
       Return: return_description
       """

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key in self.__dict__:
                    if key == "created_at" or key == "updated_at":
                        self.__dict__[key] = value.fromisoformat()
                    if key == "__class__":
                        pass
                    else:
                        self.__dict__[key] = value

        self.id = str(uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ save """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """ to dict"""
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = __class__.__name__
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                dictionary[key] = value.isoformat()
        return dictionary
