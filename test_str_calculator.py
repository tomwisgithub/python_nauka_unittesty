import unittest

from calculator import str_calculator

class TestStringCalculator(unittest.TestCase):
    def test_concat(self):
        r = str_calculator('a', 'b', 'concat')
        self.assertEqual(r, 'ab')