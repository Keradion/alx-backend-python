#!/usr/bin/env python3
""" Parametrize unittest """
import unittest
from utils import access_nested_map
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """
       The Test class inherits unittest.TestCase to acquire
       unittests class functionality.
    """
    @parameterized.expand([
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
            ])
    def test_access_nested_map(self, arg1, arg2, result):
        """ Test access_nested_map function with multiple valid inputs """
        self.assertEqual(access_nested_map(arg1, arg2), result)

    @parameterized.expand([
        ({}, "a", KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
        ])
    def test_access_nested_map_exception(self, arg1, arg2, result):
        """
            Test access_nested_map function with inputs that cause
            exception, keyError
        """
        with self.assertRaises(KeyError):
            access_nested_map(arg1, arg2)
