#!/usr/bin/env python3
""" This is a unittest for the client module """


import unittest
import client
from unittest import mock
from parameterized import parameterized


class TestGitHubOrgClient(unittest.TestCase):
    """ This class tests the Github Client """
    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @mock.patch('client.get_json',
                mock.MagicMock(return_value={'key', 'value'}))
    def test_org(self, org):
        """ this tests the org """
        tc = client.GithubOrgClient(org)
        self.assertEqual(tc.org, {'key', 'value'})


if __name__ == '__main__':
    unittest.main()
