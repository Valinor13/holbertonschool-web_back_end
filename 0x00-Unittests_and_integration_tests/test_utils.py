#!/usr/bin/env python3
""" This is a unittest for the utils module """


import unittest
import utils
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ This method tests if  the path has access to the nested map """
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)


if __name__ == '__main__':
    unittest.main()
