#!/usr/bin/python3
"""
Unittest for Place model class
"""
from models.base_model import BaseModel
import unittest
import os
from models.amenity import Amenity


class test_Amenity(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """ """
        cls.amenity1 = Amenity()
        cls.amenity1.name = "1965 Hotel"

    @classmethod
    def tearDownClass(cls):
        """ """
        del cls.amenity1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_is_subclass(self):
        """ """
        self.assertTrue(issubclass(self.amenity1.__class__, BaseModel), True)

    def test_checking_for_doc(self):
        """ """
        self.assertIsNotNone(Amenity.__doc__)

    def test_has_attributes(self):
        """ """
        self.assertTrue('id' in self.amenity1.__dict__)
        self.assertTrue('created_at' in self.amenity1.__dict__)
        self.assertTrue('updated_at' in self.amenity1.__dict__)
        self.assertTrue('name' in self.amenity1.__dict__)

    def test_attributes_are_strings(self):
        """  """
        self.assertTrue(type(self.amenity1.name), str)

    def test_save(self):
        """ """
        self.amenity1.save()
        self.assertNotEqual(self.amenity1.created_at, self.amenity1.updated_at)

    def test_to_dict(self):
        """ """
        self.assertEqual('to_dict' in dir(self.amenity1), True)


if __name__ == "__main__":
    unnittest.main()
