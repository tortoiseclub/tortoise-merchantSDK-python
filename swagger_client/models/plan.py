# coding: utf-8

"""
    Tortoise Merchant API

    Tortoise API for merchant to integrate with their existing systems   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: developer@tortoise.pro
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Plan(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'customer': 'PlanCustomer',
        'product': 'PlanProduct',
        'scheme': 'PlanScheme',
        'enrolled_on': 'datetime',
        'plan_value': 'int',
        'instalment_value': 'int',
        'total_paid_value': 'int',
        'completed_instalments': 'int',
        'next_instalment_date': 'date',
        'plan_maturity_date': 'date',
        'total_expected_redemption_value': 'int',
        'current_redemption_value': 'int',
        'current_cancellation_value': 'int',
        'last_instalment_paid_on': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'customer': 'customer',
        'product': 'product',
        'scheme': 'scheme',
        'enrolled_on': 'enrolledOn',
        'plan_value': 'planValue',
        'instalment_value': 'instalmentValue',
        'total_paid_value': 'totalPaidValue',
        'completed_instalments': 'completedInstalments',
        'next_instalment_date': 'nextInstalmentDate',
        'plan_maturity_date': 'planMaturityDate',
        'total_expected_redemption_value': 'totalExpectedRedemptionValue',
        'current_redemption_value': 'currentRedemptionValue',
        'current_cancellation_value': 'currentCancellationValue',
        'last_instalment_paid_on': 'lastInstalmentPaidOn'
    }

    def __init__(self, id=None, customer=None, product=None, scheme=None, enrolled_on=None, plan_value=None, instalment_value=None, total_paid_value=None, completed_instalments=None, next_instalment_date=None, plan_maturity_date=None, total_expected_redemption_value=None, current_redemption_value=None, current_cancellation_value=None, last_instalment_paid_on=None):  # noqa: E501
        """Plan - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._customer = None
        self._product = None
        self._scheme = None
        self._enrolled_on = None
        self._plan_value = None
        self._instalment_value = None
        self._total_paid_value = None
        self._completed_instalments = None
        self._next_instalment_date = None
        self._plan_maturity_date = None
        self._total_expected_redemption_value = None
        self._current_redemption_value = None
        self._current_cancellation_value = None
        self._last_instalment_paid_on = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if customer is not None:
            self.customer = customer
        if product is not None:
            self.product = product
        if scheme is not None:
            self.scheme = scheme
        if enrolled_on is not None:
            self.enrolled_on = enrolled_on
        if plan_value is not None:
            self.plan_value = plan_value
        if instalment_value is not None:
            self.instalment_value = instalment_value
        if total_paid_value is not None:
            self.total_paid_value = total_paid_value
        if completed_instalments is not None:
            self.completed_instalments = completed_instalments
        if next_instalment_date is not None:
            self.next_instalment_date = next_instalment_date
        if plan_maturity_date is not None:
            self.plan_maturity_date = plan_maturity_date
        if total_expected_redemption_value is not None:
            self.total_expected_redemption_value = total_expected_redemption_value
        if current_redemption_value is not None:
            self.current_redemption_value = current_redemption_value
        if current_cancellation_value is not None:
            self.current_cancellation_value = current_cancellation_value
        if last_instalment_paid_on is not None:
            self.last_instalment_paid_on = last_instalment_paid_on

    @property
    def id(self):
        """Gets the id of this Plan.  # noqa: E501

        Unique identifier for the plan  # noqa: E501

        :return: The id of this Plan.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Plan.

        Unique identifier for the plan  # noqa: E501

        :param id: The id of this Plan.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def customer(self):
        """Gets the customer of this Plan.  # noqa: E501


        :return: The customer of this Plan.  # noqa: E501
        :rtype: PlanCustomer
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this Plan.


        :param customer: The customer of this Plan.  # noqa: E501
        :type: PlanCustomer
        """

        self._customer = customer

    @property
    def product(self):
        """Gets the product of this Plan.  # noqa: E501


        :return: The product of this Plan.  # noqa: E501
        :rtype: PlanProduct
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this Plan.


        :param product: The product of this Plan.  # noqa: E501
        :type: PlanProduct
        """

        self._product = product

    @property
    def scheme(self):
        """Gets the scheme of this Plan.  # noqa: E501


        :return: The scheme of this Plan.  # noqa: E501
        :rtype: PlanScheme
        """
        return self._scheme

    @scheme.setter
    def scheme(self, scheme):
        """Sets the scheme of this Plan.


        :param scheme: The scheme of this Plan.  # noqa: E501
        :type: PlanScheme
        """

        self._scheme = scheme

    @property
    def enrolled_on(self):
        """Gets the enrolled_on of this Plan.  # noqa: E501

        Time when customer enrolled on the plan  # noqa: E501

        :return: The enrolled_on of this Plan.  # noqa: E501
        :rtype: datetime
        """
        return self._enrolled_on

    @enrolled_on.setter
    def enrolled_on(self, enrolled_on):
        """Sets the enrolled_on of this Plan.

        Time when customer enrolled on the plan  # noqa: E501

        :param enrolled_on: The enrolled_on of this Plan.  # noqa: E501
        :type: datetime
        """

        self._enrolled_on = enrolled_on

    @property
    def plan_value(self):
        """Gets the plan_value of this Plan.  # noqa: E501

        Total price of the plan, to be paid by the customer  # noqa: E501

        :return: The plan_value of this Plan.  # noqa: E501
        :rtype: int
        """
        return self._plan_value

    @plan_value.setter
    def plan_value(self, plan_value):
        """Sets the plan_value of this Plan.

        Total price of the plan, to be paid by the customer  # noqa: E501

        :param plan_value: The plan_value of this Plan.  # noqa: E501
        :type: int
        """

        self._plan_value = plan_value

    @property
    def instalment_value(self):
        """Gets the instalment_value of this Plan.  # noqa: E501

        Value of each instalment to be paid by the customer  # noqa: E501

        :return: The instalment_value of this Plan.  # noqa: E501
        :rtype: int
        """
        return self._instalment_value

    @instalment_value.setter
    def instalment_value(self, instalment_value):
        """Sets the instalment_value of this Plan.

        Value of each instalment to be paid by the customer  # noqa: E501

        :param instalment_value: The instalment_value of this Plan.  # noqa: E501
        :type: int
        """

        self._instalment_value = instalment_value

    @property
    def total_paid_value(self):
        """Gets the total_paid_value of this Plan.  # noqa: E501

        Total amount paid by the customer towards the plan till date  # noqa: E501

        :return: The total_paid_value of this Plan.  # noqa: E501
        :rtype: int
        """
        return self._total_paid_value

    @total_paid_value.setter
    def total_paid_value(self, total_paid_value):
        """Sets the total_paid_value of this Plan.

        Total amount paid by the customer towards the plan till date  # noqa: E501

        :param total_paid_value: The total_paid_value of this Plan.  # noqa: E501
        :type: int
        """

        self._total_paid_value = total_paid_value

    @property
    def completed_instalments(self):
        """Gets the completed_instalments of this Plan.  # noqa: E501

        Instalments paid by customer till date  # noqa: E501

        :return: The completed_instalments of this Plan.  # noqa: E501
        :rtype: int
        """
        return self._completed_instalments

    @completed_instalments.setter
    def completed_instalments(self, completed_instalments):
        """Sets the completed_instalments of this Plan.

        Instalments paid by customer till date  # noqa: E501

        :param completed_instalments: The completed_instalments of this Plan.  # noqa: E501
        :type: int
        """

        self._completed_instalments = completed_instalments

    @property
    def next_instalment_date(self):
        """Gets the next_instalment_date of this Plan.  # noqa: E501

        Due date for the upcoming instalment of the plan  # noqa: E501

        :return: The next_instalment_date of this Plan.  # noqa: E501
        :rtype: date
        """
        return self._next_instalment_date

    @next_instalment_date.setter
    def next_instalment_date(self, next_instalment_date):
        """Sets the next_instalment_date of this Plan.

        Due date for the upcoming instalment of the plan  # noqa: E501

        :param next_instalment_date: The next_instalment_date of this Plan.  # noqa: E501
        :type: date
        """

        self._next_instalment_date = next_instalment_date

    @property
    def plan_maturity_date(self):
        """Gets the plan_maturity_date of this Plan.  # noqa: E501

        Date on which the plan is expected to mature  # noqa: E501

        :return: The plan_maturity_date of this Plan.  # noqa: E501
        :rtype: date
        """
        return self._plan_maturity_date

    @plan_maturity_date.setter
    def plan_maturity_date(self, plan_maturity_date):
        """Sets the plan_maturity_date of this Plan.

        Date on which the plan is expected to mature  # noqa: E501

        :param plan_maturity_date: The plan_maturity_date of this Plan.  # noqa: E501
        :type: date
        """

        self._plan_maturity_date = plan_maturity_date

    @property
    def total_expected_redemption_value(self):
        """Gets the total_expected_redemption_value of this Plan.  # noqa: E501

        Total amount expected to be redeemed by the customer at the end of the plan  # noqa: E501

        :return: The total_expected_redemption_value of this Plan.  # noqa: E501
        :rtype: int
        """
        return self._total_expected_redemption_value

    @total_expected_redemption_value.setter
    def total_expected_redemption_value(self, total_expected_redemption_value):
        """Sets the total_expected_redemption_value of this Plan.

        Total amount expected to be redeemed by the customer at the end of the plan  # noqa: E501

        :param total_expected_redemption_value: The total_expected_redemption_value of this Plan.  # noqa: E501
        :type: int
        """

        self._total_expected_redemption_value = total_expected_redemption_value

    @property
    def current_redemption_value(self):
        """Gets the current_redemption_value of this Plan.  # noqa: E501

        Total amount that can be redeemed by the customer by closing the plan today  # noqa: E501

        :return: The current_redemption_value of this Plan.  # noqa: E501
        :rtype: int
        """
        return self._current_redemption_value

    @current_redemption_value.setter
    def current_redemption_value(self, current_redemption_value):
        """Sets the current_redemption_value of this Plan.

        Total amount that can be redeemed by the customer by closing the plan today  # noqa: E501

        :param current_redemption_value: The current_redemption_value of this Plan.  # noqa: E501
        :type: int
        """

        self._current_redemption_value = current_redemption_value

    @property
    def current_cancellation_value(self):
        """Gets the current_cancellation_value of this Plan.  # noqa: E501

        Total amount that is paid back to customer if the plan is cancelled today  # noqa: E501

        :return: The current_cancellation_value of this Plan.  # noqa: E501
        :rtype: int
        """
        return self._current_cancellation_value

    @current_cancellation_value.setter
    def current_cancellation_value(self, current_cancellation_value):
        """Sets the current_cancellation_value of this Plan.

        Total amount that is paid back to customer if the plan is cancelled today  # noqa: E501

        :param current_cancellation_value: The current_cancellation_value of this Plan.  # noqa: E501
        :type: int
        """

        self._current_cancellation_value = current_cancellation_value

    @property
    def last_instalment_paid_on(self):
        """Gets the last_instalment_paid_on of this Plan.  # noqa: E501

        Timestamp of last paid instalment  # noqa: E501

        :return: The last_instalment_paid_on of this Plan.  # noqa: E501
        :rtype: datetime
        """
        return self._last_instalment_paid_on

    @last_instalment_paid_on.setter
    def last_instalment_paid_on(self, last_instalment_paid_on):
        """Sets the last_instalment_paid_on of this Plan.

        Timestamp of last paid instalment  # noqa: E501

        :param last_instalment_paid_on: The last_instalment_paid_on of this Plan.  # noqa: E501
        :type: datetime
        """

        self._last_instalment_paid_on = last_instalment_paid_on

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Plan, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Plan):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
