# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.new_user_request_body import NewUserRequestBody  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_get_user_by_id(self):
        """Test case for get_user_by_id

        
        """
        response = self.client.open(
            '/api/users/{userID}'.format(user_id='user_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_users(self):
        """Test case for get_users

        
        """
        response = self.client.open(
            '/api/users/',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_new_user(self):
        """Test case for post_new_user

        
        """
        body = NewUserRequestBody()
        response = self.client.open(
            '/api/users/newUser',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_users(self):
        """Test case for search_users

        
        """
        query_string = [('search_string', 'search_string_example')]
        response = self.client.open(
            '/api/users/fuzzysearch',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
