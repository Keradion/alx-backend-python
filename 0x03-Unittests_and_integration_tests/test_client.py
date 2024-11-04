#!/usr/bin/env python3
import unittest
from utils import access_nested_map, get_json, memoize
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import patch, MagicMock


class TestGithubOrgClient(unittest.TestCase):
    """Test class for TestGithubOrgClient"""
    @parameterized.expand([
        ('google'),
        ('abc')
        ])
    @patch('client.get_json')
    def test_org(self, parameter, mock_get_json):
        """
           Test org() if it returns a correct value
           Test get_json is called once with the expected arg
           make sure get_json is not executed
        """

        url = "https://api.github.com/orgs/{}".format(parameter)

        # This method should test GithubOrgClient.org()
        my_object = GithubOrgClient(parameter)
        my_object.org()

        # Use @patch as a decorator to make sure get_json is called once
        mock_get_json.assert_called_once_with(url)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, 'my_license', True),
        ({"license": {"key": "other_license"}}, 'my_license', False)
        ])
    def test_has_license(self, parameter1, parameter2,  expected_result):
        """ Test case for has_license """
        self.assertEqual(GithubOrgClient.has_license(
            parameter1, parameter2), expected_result)
