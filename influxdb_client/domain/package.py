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


class Package(object):
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
        'type': 'str',
        'path': 'str',
        'package': 'str',
        'files': 'list[File]'
    }

    attribute_map = {
        'type': 'type',
        'path': 'path',
        'package': 'package',
        'files': 'files'
    }

    def __init__(self, type=None, path=None, package=None, files=None):  # noqa: E501
        """Package - a model defined in OpenAPI"""  # noqa: E501

        self._type = None
        self._path = None
        self._package = None
        self._files = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if path is not None:
            self.path = path
        if package is not None:
            self.package = package
        if files is not None:
            self.files = files

    @property
    def type(self):
        """Gets the type of this Package.  # noqa: E501

        Type of AST node  # noqa: E501

        :return: The type of this Package.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Package.

        Type of AST node  # noqa: E501

        :param type: The type of this Package.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def path(self):
        """Gets the path of this Package.  # noqa: E501

        Package import path  # noqa: E501

        :return: The path of this Package.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this Package.

        Package import path  # noqa: E501

        :param path: The path of this Package.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def package(self):
        """Gets the package of this Package.  # noqa: E501

        Package name  # noqa: E501

        :return: The package of this Package.  # noqa: E501
        :rtype: str
        """
        return self._package

    @package.setter
    def package(self, package):
        """Sets the package of this Package.

        Package name  # noqa: E501

        :param package: The package of this Package.  # noqa: E501
        :type: str
        """

        self._package = package

    @property
    def files(self):
        """Gets the files of this Package.  # noqa: E501

        Package files  # noqa: E501

        :return: The files of this Package.  # noqa: E501
        :rtype: list[File]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this Package.

        Package files  # noqa: E501

        :param files: The files of this Package.  # noqa: E501
        :type: list[File]
        """

        self._files = files

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
        if not isinstance(other, Package):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
