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


class Scheme(object):
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
        'name': 'str',
        'created_on': 'datetime',
        'status': 'str',
        'redemption_option': 'SchemeRedemptionOption',
        'duration_in_months': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'created_on': 'createdOn',
        'status': 'status',
        'redemption_option': 'redemptionOption',
        'duration_in_months': 'durationInMonths'
    }

    def __init__(self, id=None, name=None, created_on=None, status=None, redemption_option=None, duration_in_months=None):  # noqa: E501
        """Scheme - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._created_on = None
        self._status = None
        self._redemption_option = None
        self._duration_in_months = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if created_on is not None:
            self.created_on = created_on
        if status is not None:
            self.status = status
        if redemption_option is not None:
            self.redemption_option = redemption_option
        if duration_in_months is not None:
            self.duration_in_months = duration_in_months

    @property
    def id(self):
        """Gets the id of this Scheme.  # noqa: E501

        Unique identifier for the scheme  # noqa: E501

        :return: The id of this Scheme.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Scheme.

        Unique identifier for the scheme  # noqa: E501

        :param id: The id of this Scheme.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Scheme.  # noqa: E501

        Name of the scheme  # noqa: E501

        :return: The name of this Scheme.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Scheme.

        Name of the scheme  # noqa: E501

        :param name: The name of this Scheme.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def created_on(self):
        """Gets the created_on of this Scheme.  # noqa: E501

        Timestamp at which the scheme is created  # noqa: E501

        :return: The created_on of this Scheme.  # noqa: E501
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this Scheme.

        Timestamp at which the scheme is created  # noqa: E501

        :param created_on: The created_on of this Scheme.  # noqa: E501
        :type: datetime
        """

        self._created_on = created_on

    @property
    def status(self):
        """Gets the status of this Scheme.  # noqa: E501


        :return: The status of this Scheme.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Scheme.


        :param status: The status of this Scheme.  # noqa: E501
        :type: str
        """
        allowed_values = ["active", "disabled", "reviewPending", "reviewRejected"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def redemption_option(self):
        """Gets the redemption_option of this Scheme.  # noqa: E501


        :return: The redemption_option of this Scheme.  # noqa: E501
        :rtype: SchemeRedemptionOption
        """
        return self._redemption_option

    @redemption_option.setter
    def redemption_option(self, redemption_option):
        """Sets the redemption_option of this Scheme.


        :param redemption_option: The redemption_option of this Scheme.  # noqa: E501
        :type: SchemeRedemptionOption
        """

        self._redemption_option = redemption_option

    @property
    def duration_in_months(self):
        """Gets the duration_in_months of this Scheme.  # noqa: E501

        Duration of the scheme in months, in other words, number of instalments to be paid by the customer  # noqa: E501

        :return: The duration_in_months of this Scheme.  # noqa: E501
        :rtype: int
        """
        return self._duration_in_months

    @duration_in_months.setter
    def duration_in_months(self, duration_in_months):
        """Sets the duration_in_months of this Scheme.

        Duration of the scheme in months, in other words, number of instalments to be paid by the customer  # noqa: E501

        :param duration_in_months: The duration_in_months of this Scheme.  # noqa: E501
        :type: int
        """

        self._duration_in_months = duration_in_months

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
        if issubclass(Scheme, dict):
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
        if not isinstance(other, Scheme):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
