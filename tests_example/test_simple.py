import unittest
from unittest.mock import patch, Mock


def func_to_test(value_in):
    return value_in+2


class TestExample(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_some_data(self):
        test_value = func_to_test(1)
        self.assertEqual(3, test_value)
