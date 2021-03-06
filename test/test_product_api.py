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
from swagger_client.api.product_api import ProductApi  # noqa: E501
from swagger_client.rest import ApiException


class TestProductApi(unittest.TestCase):
    """ProductApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.product_api.ProductApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_product(self):
        """Test case for add_product

        Add a new product  # noqa: E501
        """
        pass

    def test_edit_product(self):
        """Test case for edit_product

        Edit product details  # noqa: E501
        """
        pass

    def test_fetch_all_products(self):
        """Test case for fetch_all_products

        Fetch all products  # noqa: E501
        """
        pass

    def test_get_product(self):
        """Test case for get_product

        Get product by ID  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
