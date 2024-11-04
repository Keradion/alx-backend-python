#!/usr/bin/env python3
""" Parametrize unittest """
import unittest
from utils import access_nested_map, get_json, memoize
from client import GithubOrgClient
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


class TestMemoize(unittest.TestCase):
    """This class holds test for utils.memoize decorator"""
    def test_memoize(self):
        """
           Test case that use unittest.mock.patch to mock a_method.
           Test that when calling a_property twice ...
           a_method is only called once using assert_called_once.
        """
        class TestClass:
            def a_method(self):
                return 42
            
            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_method:
            # Set the return value of the patched methods as 42
            mock_method.return_value = 42
            # Instance of TestClass to call a_property
            my_object = TestClass()
            # Call a_property method twice
            result1 = my_object.a_property
            result2 = my_object.a_property
            # Assert a_method called only once
            mock_method.assert_called_once()
            # Assert the return value is correct
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

class TestGithubOrgClient(unittest.TestCase):
    """ """
    @parameterized.expand([
        ('google'), 
        ('abc')
        ])
    @patch('client.get_json')
    def test_org(self, parameter, mock_get_json):
        """ Test org() if it returns a correct value """
        """ Test get_json is called once with the expected arg """
        """ make sure get_json is not executed """
        
        url = "https://api.github.com/orgs/{}".format(parameter)
        
        # This method should test that GithubOrgClient.org returns the correct value.
        my_object = GithubOrgClient(parameter)
        my_object.org()
        
        # Use @patch as a decorator to make sure get_json is called once with the expected argument but make sure it is not executed.
        mock_get_json.assert_called_once_with(url)

