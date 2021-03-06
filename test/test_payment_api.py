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
from swagger_client.api.payment_api import PaymentApi  # noqa: E501
from swagger_client.rest import ApiException


class TestPaymentApi(unittest.TestCase):
    """PaymentApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.payment_api.PaymentApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_payment(self):
        """Test case for add_payment

        Add a new payment  # noqa: E501
        """
        pass

    def test_fetch_all_payments(self):
        """Test case for fetch_all_payments

        Fetch all payments  # noqa: E501
        """
        pass

    def test_get_payment(self):
        """Test case for get_payment

        Get payment by ID  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
