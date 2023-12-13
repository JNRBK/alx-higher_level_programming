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

        a2 = Rectangle(1, 2, 3)
        self.assertEqual(a2.width, 1)
        self.assertEqual(a2.height, 2)
        self.assertEqual(a2.x, 3)

    def test_width_and_height(self):
        w_h = Rectangle(1, 2)
        self.assertRaises(TypeError, Rectangle, "1", 2)
        self.assertRaises(TypeError, Rectangle, 1, "2")

        self.assertRaises(TypeError, Rectangle, None, 2)
        self.assertRaises(TypeError, Rectangle, 1, None)

        self.assertRaises(ValueError, Rectangle, -1, 2)
        self.assertRaises(ValueError, Rectangle, 1, -2)

        self.assertRaises(ValueError, Rectangle, 0, 2)
        self.assertRaises(ValueError, Rectangle, 1, 0)

    def test_x_and_y(self):
        x_y = Rectangle(1, 2, 3, 4)
        self.assertRaises(TypeError, Rectangle, 1, 2, "3", 4)
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, "4")

        self.assertRaises(TypeError, Rectangle, 1, 2, None, 4)
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, None)

        self.assertRaises(ValueError, Rectangle, 1, 2, -3, 4)
        self.assertRaises(ValueError, Rectangle, 1, 2, 3, -4)

    def test_rectangle_area(self):
        ar = Rectangle(4, 5)
        ar1 = Rectangle(6, 5)
        self.assertEqual(ar.area(), 20)
        self.assertEqual(ar1.area(), 30)
