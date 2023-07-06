#!/usr/bin/python3
"""
sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""
from json import dump, load, loads
import os.path


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        FileStorage.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """storage in file.json"""
        with open(self.__file_path, "w") as f:
            dictionary = {}
            if len(FileStorage.__objects) > 0:
                for key, value in FileStorage.__objects.items():
                    dictionary[key] = value.to_dict()
                dump(dictionary, f)

    def reload(self):
        """ reload from file.json"""
        from models.base_model import BaseModel
        if os.path.exists(self.__file_path):
            with open(FileStorage.__file_path, "r") as fle:
                diccionario = load(fle)
                for key, value in diccionario.items():
                    a = value["__class__"]
                    instancia_objeto = BaseModel(**value)
                    self.__objects[key] = instancia_objeto
