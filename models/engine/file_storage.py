#!/usr/bin/python3
"""sumary_line

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
        self.__objects[obj.__class__name__ + "." + obj.id] = obj

    def save(self):
        with open(self.__file_path, "a") as f:
            dump(self.obj, f)

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as fle:
                a = load(self.__file_path)
                self.__objects = a
        else:
            pass