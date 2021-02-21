#!/usr/bin/python3
"""
    unitest for base_model
"""
import unittest
from models.base_model import BaseModel


class test_Base_Model(unittest.TestCase):

    def test_save(self):
        e = BaseModel()
        s = e.updated_at
        e.save()
        self.assertNotEqual(s, e.updated_at)

    def test_to_dict(self):
        e = BaseModel()
        x = e.__dict__
        self.assertIsNotNone(e.to_dict())

    def test_id(self):
        e = BaseModel()
        self.assertIsNotNone(self.id)

    def test_created_at(self):
        e = BaseModel()
        self.assertIsNotNone(e.created_at)

    def test___str__(self):
        e = BaseModel()
        x = ("[{}] ({}) {}".format(e.__class__.__name__,
                                   e.id, e.__dict__))
        self.assertEqual(x, e.__str__())
