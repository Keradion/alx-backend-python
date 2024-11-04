import unittest
from utils import access_nested_map, get_json, memoize
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import patch, MagicMock


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
