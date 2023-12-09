# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class NewUserRequestBody(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, first_name: str=None, last_name: str=None, password: str=None, email: str=None):  # noqa: E501
        """NewUserRequestBody - a model defined in Swagger

        :param first_name: The first_name of this NewUserRequestBody.  # noqa: E501
        :type first_name: str
        :param last_name: The last_name of this NewUserRequestBody.  # noqa: E501
        :type last_name: str
        :param password: The password of this NewUserRequestBody.  # noqa: E501
        :type password: str
        :param email: The email of this NewUserRequestBody.  # noqa: E501
        :type email: str
        """
        self.swagger_types = {
            'first_name': str,
            'last_name': str,
            'password': str,
            'email': str
        }

        self.attribute_map = {
            'first_name': 'first_name',
            'last_name': 'last_name',
            'password': 'password',
            'email': 'email'
        }
        self._first_name = first_name
        self._last_name = last_name
        self._password = password
        self._email = email

    @classmethod
    def from_dict(cls, dikt) -> 'NewUserRequestBody':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The new_user_request_body of this NewUserRequestBody.  # noqa: E501
        :rtype: NewUserRequestBody
        """
        return util.deserialize_model(dikt, cls)

    @property
    def first_name(self) -> str:
        """Gets the first_name of this NewUserRequestBody.


        :return: The first_name of this NewUserRequestBody.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str):
        """Sets the first_name of this NewUserRequestBody.


        :param first_name: The first_name of this NewUserRequestBody.
        :type first_name: str
        """
        if first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")  # noqa: E501

        self._first_name = first_name

    @property
    def last_name(self) -> str:
        """Gets the last_name of this NewUserRequestBody.


        :return: The last_name of this NewUserRequestBody.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        """Sets the last_name of this NewUserRequestBody.


        :param last_name: The last_name of this NewUserRequestBody.
        :type last_name: str
        """
        if last_name is None:
            raise ValueError("Invalid value for `last_name`, must not be `None`")  # noqa: E501

        self._last_name = last_name

    @property
    def password(self) -> str:
        """Gets the password of this NewUserRequestBody.


        :return: The password of this NewUserRequestBody.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password: str):
        """Sets the password of this NewUserRequestBody.


        :param password: The password of this NewUserRequestBody.
        :type password: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def email(self) -> str:
        """Gets the email of this NewUserRequestBody.


        :return: The email of this NewUserRequestBody.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this NewUserRequestBody.


        :param email: The email of this NewUserRequestBody.
        :type email: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email