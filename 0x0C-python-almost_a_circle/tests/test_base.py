import unittest
from models.base import Base
from models.square import Square

class base_test(unittest.TestCase):
    def test_args(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)
