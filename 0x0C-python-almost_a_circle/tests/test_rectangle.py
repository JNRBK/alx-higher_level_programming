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
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 2)

        a1 = Rectangle(1, 2, 5)
        self.assertEqual(a1.width, 1)
        self.assertEqual(a1.height, 2)
        self.assertEqual(a1.x, 5)
        self.assertEqual(a1.y, 0)
        self.assertEqual(a1.id, 3)

        s1 = Rectangle(1, 2, 5, 4)
        self.assertEqual(s1.width, 1)
        self.assertEqual(s1.height, 2)
        self.assertEqual(s1.x, 5)
        self.assertEqual(s1.y, 4)
        self.assertEqual(s1.id, 4)

        with self.assertRaises(TypeError):
            err = Rectangle("1", 2)
