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
from swagger_client.api.plan_api import PlanApi  # noqa: E501
from swagger_client.rest import ApiException


class TestPlanApi(unittest.TestCase):
    """PlanApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.plan_api.PlanApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_plan(self):
        """Test case for add_plan

        Add a new plan  # noqa: E501
        """
        pass

    def test_edit_plan(self):
        """Test case for edit_plan

        Edit a plan's details  # noqa: E501
        """
        pass

    def test_fetch_all_plans(self):
        """Test case for fetch_all_plans

        Fetch all plans  # noqa: E501
        """
        pass

    def test_get_plan(self):
        """Test case for get_plan

        Get a plan by ID  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
