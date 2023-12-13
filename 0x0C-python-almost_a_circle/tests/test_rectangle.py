import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
import json


class Test_Rectangle(unittest.TestCase):

    def test_rectangle(self):
        rec = Rectangle(10, 5)
        self.assertEqual(rec.area(), 50)
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
