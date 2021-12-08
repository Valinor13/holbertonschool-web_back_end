#!/usr/bin/env python3
""" This is a unittest for the client module """


import unittest
import client
from unittest import mock
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """ This class tests the Github Client """
    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @mock.patch('client.get_json', mock.MagicMock(return_value={'a': 1}))
    def test_org(self, org):
        """ this tests the org """
        tc = client.GithubOrgClient(org)
        self.assertEqual(tc.org, {'a': 1})

    @client.memoize
    def test_public_repos_url(self):
        """ test GithubOrgClient for consistent return """
        with mock.patch('client.GithubOrgClient.org',
                        mock.MagicMock(return_value={'a': 1})):
            tc = client.GithubOrgClient('org_name')
            self.assertEqual(tc._public_repos_url, 1)

    @mock.patch('client.get_json')
    def test_public_repos(self, org):
        """ tests if public repos exist with correct mock info """
        with mock.patch('client.GithubOrgClient.public_repos',
                        new_callable=mock.PropertyMock) as mocker:
            tc = client.GithubOrgClient('org_name')
            new_mock = mocker()
            mocker.assert_called_once()
            self.assertEqual(tc.public_repos, new_mock)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """ tests if the license exists in the repo """
        tc = client.GithubOrgClient('org_name')
        self.assertEqual(tc.has_license(repo, license_key), expected)


if __name__ == '__main__':
    unittest.main()
