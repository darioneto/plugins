# coding: utf-8

"""
    Influx API Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class RunLog(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'run_id': 'str',
        'time': 'str',
        'message': 'str'
    }

    attribute_map = {
        'run_id': 'runID',
        'time': 'time',
        'message': 'message'
    }

    def __init__(self, run_id=None, time=None, message=None):  # noqa: E501
        """RunLog - a model defined in OpenAPI"""  # noqa: E501

        self._run_id = None
        self._time = None
        self._message = None
        self.discriminator = None

        if run_id is not None:
            self.run_id = run_id
        if time is not None:
            self.time = time
        if message is not None:
            self.message = message

    @property
    def run_id(self):
        """Gets the run_id of this RunLog.  # noqa: E501


        :return: The run_id of this RunLog.  # noqa: E501
        :rtype: str
        """
        return self._run_id

    @run_id.setter
    def run_id(self, run_id):
        """Sets the run_id of this RunLog.


        :param run_id: The run_id of this RunLog.  # noqa: E501
        :type: str
        """

        self._run_id = run_id

    @property
    def time(self):
        """Gets the time of this RunLog.  # noqa: E501


        :return: The time of this RunLog.  # noqa: E501
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this RunLog.


        :param time: The time of this RunLog.  # noqa: E501
        :type: str
        """

        self._time = time

    @property
    def message(self):
        """Gets the message of this RunLog.  # noqa: E501


        :return: The message of this RunLog.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this RunLog.


        :param message: The message of this RunLog.  # noqa: E501
        :type: str
        """

        self._message = message

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RunLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
