#!/usr/bin/env python3
""" Parametrize unittest """
import unittest
from utils import access_nested_map, get_json
from parameterized import parameterized
from unittest.mock import patch, MagicMock


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


class TestGetJson(unittest.TestCase):
    """
       The test class inherits from unittest and consist
       Multiple Test for get_json() from utils class.
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}), 
        ("http://holberton.io", {"payload": False}),
        ])
    @patch('utils.requests')
    def test_get_json(self, test_url, test_payload, mock_request):
        """Test get_json method of utils http calls."""
        # Create a mock for http response object
        mock_response = MagicMock()

        # Set status_code for http response object
        mock_response.status_code = 200

        # Set return value for Json() of http response object
        mock_response.json.return_value = test_payload

        mock_request.get.return_value = mock_response

        self.assertEqual(get_json(test_url), test_payload)
        mock_request.get.assert_called_once()
