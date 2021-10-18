#!/user/bin/python3
import unittest
import json
import io
import sys
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle_instantiation(unittest.TestCase):
    """unitest for checking rectangle instantiation"""

    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(10, 2), Base)
