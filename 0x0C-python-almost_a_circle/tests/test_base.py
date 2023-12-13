import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
import json


class TestBase(unittest.TestCase):
    def test_Base(self):
        b = Base()
        self.assertEqual(b.id, 1)
        b1 = Base(89)
        self.assertEqual(b1.id, 89)
        b2 = Base()
        b3 = Base()
        self.assertEqual(b2.id + 1, b3.id)

    def test_json_string(self):
        tjson = Base.to_json_string([])
        self.assertEqual(tjson, "[]")
        tjson = Base.to_json_string(None)
        self.assertEqual(tjson, '[]')
        data = [{'id': 12}]
        tjson = Base.to_json_string(data)
        ex = json.dumps(data)
        self.assertEqual(tjson, ex)

    def test_from_json_string(self):
        fjson = Base.from_json_string('')
        self.assertEqual(fjson, [])
        fjson1 = Base.from_json_string(None)
        self.assertEqual(fjson1, [])
        fj = Base.from_json_string("[]")
        self.assertEqual(fj, [])
        data = ('[{"id": 89}]')
        fjson2 = Base.from_json_string(data)
        ex = json.loads(data)
        self.assertEqual(fjson2, ex)
