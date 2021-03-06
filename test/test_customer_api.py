# coding: utf-8

"""
    Tortoise Merchant API

    Tortoise API for merchant to integrate with their existing systems   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: developer@tortoise.pro
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.customer_api import CustomerApi  # noqa: E501
from swagger_client.rest import ApiException


class TestCustomerApi(unittest.TestCase):
    """CustomerApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.customer_api.CustomerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_customer(self):
        """Test case for add_customer

        Add a new customer  # noqa: E501
        """
        pass

    def test_edit_customer(self):
        """Test case for edit_customer

        Edit customer details  # noqa: E501
        """
        pass

    def test_fetch_all_customers(self):
        """Test case for fetch_all_customers

        Fetch all customers  # noqa: E501
        """
        pass

    def test_get_customer(self):
        """Test case for get_customer

        Get customer by ID  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
