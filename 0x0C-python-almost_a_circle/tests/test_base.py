import unittest
from models.base import Base
from models.square import Square

class base_test(unittest.TestCase):
    def test_Base(self):
        b = Base()
        self.assertEqual(b.id, 1)
        b1 = Base()
        b1.id = 1
        self.assertEqual(b1.id, 1)
        b2 = Base()
        b3 = Base()
        self.assertEqual(b2.id + 1, b3.id)
