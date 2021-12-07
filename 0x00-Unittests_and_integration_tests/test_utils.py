#!/usr/bin/env python3
""" This is a unittest for the utils module """


import unittest
import utils
from unittest import mock
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ This method tests if the path has access to the nested map """
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """ This method tests access path function for key error """
        self.assertRaises(expected, utils.access_nested_map, nested_map, path)


class TestGetJson(unittest.TestCase):
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """ this method tests the request for url in json """
        with mock.patch('utils.get_json', return_value=test_payload):
            self.assertEqual(utils.get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    """ Test class
    direct cause of pain and suffering """

    def test_memoize(self):
        """ Tests memoize method """
        class TestClass:
            """ class """

            def a_method(self):
                """ method  """
                return 42

            @utils.memoize
            def a_property(self):
                """ property """
                return self.a_method()
        with mock.patch.object(TestClass, "a_method") as mockMethod:
            test_class = TestClass()
            test_class.a_property
            test_class.a_property
            mockMethod.assert_called_once


if __name__ == '__main__':
    unittest.main()
