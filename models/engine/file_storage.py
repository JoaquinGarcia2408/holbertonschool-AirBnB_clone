#!/usr/bin/python3
"""
clase para almacenar todo
"""
from json import dump, load, loads
import os.path


class FileStorage:
    """ clase para guardar los objetos
    de python en formato json en un archivo.
    esta clase tambien ofrece metodos
    para convertir json en instancias de clase"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return self.__objects"""
        return self.__objects

    def new(self, obj):
        """ agrega un nuevo key/value a __objects"""
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
                    instancia_objeto = eval(a + '(**value)')
                    self.__objects[key] = instancia_objeto
        else:
            pass