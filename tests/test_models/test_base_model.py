#!/usr/bin/python3
"""
Aca van todos los test
que se le ejecutaran
a la clase base/
"""


import unittest
import models
from models.base_model import BaseModel
from datetime import datetime
from time import sleep
import os


class TestBaseModel(unittest.TestCase):
    """ testing for basemodel"""

    def test_id(self):
        """ base models"""
        b = BaseModel()
        b1 = BaseModel()
        self.assertNotEqual(b.id, b1.id)

    def test_dict(self):
        """ to dict"""
        r1 = BaseModel()
        r1_dictionary = r1.to_dict()
        self.assertEqual(isinstance(r1_dictionary, dict), True)
        self.assertEqual(str(type(r1_dictionary)), "<class 'dict'>")

    def test_to_save(self):
        """test save"""
        upd = BaseModel()
        b = upd.updated_at
        upd.save()
        c = upd.updated_at
        self.assertNotEqual(b, c)

    def test_created_at(self):
        """ tests created"""
        ud = BaseModel()
        b = datetime.now()
        c = ud.created_at
        self.assertNotEqual(c, b)


class TestBaseModel_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    def test_no_args(self):
        """ no args"""
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored(self):
        """ test"""
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id(self):
        """test type"""
        self.assertEqual(str, type(BaseModel().id))

    def test_created_isdatetime(self):
        """test """
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_datetime(self):
        """test"""
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_created_at(self):
        """a seguir probando"""
        b = BaseModel()
        sleep(0.05)
        b1 = BaseModel()
        self.assertLess(b.created_at, b1.created_at)

    def test_two_models_different_updated_at(self):
        """try again"""
        b = BaseModel()
        sleep(0.05)
        b1 = BaseModel()
        self.assertLess(b.updated_at, b1.updated_at)

    def test_str_representation(self):
        """ again """
        dt = datetime.today()
        dt_repr = repr(dt)
        b = BaseModel()
        b.id = "123456"
        b.created_at = b.updated_at = dt
        bstr = b.__str__()
        self.assertIn("[BaseModel] (123456)", bstr)
        self.assertIn("'id': '123456'", bstr)
        self.assertIn("'created_at': " + dt_repr, bstr)
        self.assertIn("'updated_at': " + dt_repr, bstr)

    def test_args_unused(self):
        """ coment or dead"""
        bm = BaseModel(None)
        self.assertNotIn(None, bm.__dict__.values())

    def test_with_kwargs(self):
        """ kwargs"""
        dt = datetime.now()
        dt_iso = dt.isoformat()
        b = BaseModel(id="11111", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(b.id, "11111")
        self.assertEqual(b.created_at, dt)
        self.assertEqual(b.updated_at, dt)
        self.assertEqual(b.created_at, b.updated_at)


class TestBaseModel_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the BaseModel class."""

    def test_to_dict_type(self):
        """test type"""
        b = BaseModel()
        self.assertTrue(dict, type(b.to_dict()))

    def test_to_dict_contains_all_keys(self):
        """ all keys?"""
        b = BaseModel()
        b.name = "martin"
        b.my_number = 34
        self.assertIn("id", b.to_dict())
        self.assertIn("created_at", b.to_dict())
        self.assertIn("updated_at", b.to_dict())
        self.assertIn("__class__", b.to_dict())
        self.assertIn("name", b.to_dict())
        self.assertIn("my_number", b.to_dict())

    def test_to_dict_contains_attributes(self):
        """ hello"""
        b = BaseModel()
        b.name = "Martin"
        b.my_number = 34
        self.assertIn("name", b.to_dict())
        self.assertIn("my_number", b.to_dict())


if __name__ == "__main__":
    unittest.main()
