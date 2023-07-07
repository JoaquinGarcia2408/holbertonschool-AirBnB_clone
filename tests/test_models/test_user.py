#!/usr/bin/python3
"""
todos los test para la clase
user
"""

import unittest
from models.user import User
from models.base_model import BaseModel

class TestUser(unittest.TestCase):
    """tests for class user
    """
    def test_id(self):
        usuario = User()
        usuario2 = User()
        self.assertNotEqual(usuario, usuario2)
        self.assertEqual(usuario2==usuario, False)
        self.assertEqual(usuario is usuario2, False)
    
    def test_todict(self):
        usuario = User()
        usuario_dict = usuario.to_dict()
        usuario1 = User(usuario_dict)
        self.assertEqual(usuario==usuario1, False)
        self.assertEqual(usuario is usuario1, False)

    def test_instance(self):
        usuario = User()
        self.assertIsInstance(usuario, User)

    def test_inheritance(self):
        usuario = User()
        self.assertTrue(issubclass(User, BaseModel))

    def test_atributos(self):
        usuario = User()
        self.assertIn("id", usuario.to_dict())
        usuario.email = "martin@gmail.com"
        usuario.password = "root"
        usuario.first_name = "martin"
        usuario.last_name = "Elias"
        self.assertIn("email", usuario.__dict__)
        self.assertIn("email", usuario.to_dict())
        self.assertIn("password", usuario.to_dict())
        self.assertIn("password", usuario.__dict__)
        self.assertIn("first_name", usuario.to_dict())
        self.assertIn("first_name", usuario.__dict__)
        self.assertIn("last_name", usuario.to_dict())
        self.assertIn("last_name", usuario.__dict__)
        self.assertIn("id", usuario.to_dict())
        self.assertIn("id", usuario.__dict__)
        