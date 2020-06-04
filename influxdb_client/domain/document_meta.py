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


class DocumentMeta(object):
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
        'name': 'str',
        'type': 'str',
        'template_id': 'str',
        'description': 'str',
        'version': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'template_id': 'templateID',
        'description': 'description',
        'version': 'version',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt'
    }

    def __init__(self, name=None, type=None, template_id=None, description=None, version=None, created_at=None, updated_at=None):  # noqa: E501
        """DocumentMeta - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._type = None
        self._template_id = None
        self._description = None
        self._version = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.name = name
        if type is not None:
            self.type = type
        if template_id is not None:
            self.template_id = template_id
        if description is not None:
            self.description = description
        self.version = version
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def name(self):
        """Gets the name of this DocumentMeta.  # noqa: E501


        :return: The name of this DocumentMeta.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DocumentMeta.


        :param name: The name of this DocumentMeta.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this DocumentMeta.  # noqa: E501


        :return: The type of this DocumentMeta.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DocumentMeta.


        :param type: The type of this DocumentMeta.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def template_id(self):
        """Gets the template_id of this DocumentMeta.  # noqa: E501


        :return: The template_id of this DocumentMeta.  # noqa: E501
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this DocumentMeta.


        :param template_id: The template_id of this DocumentMeta.  # noqa: E501
        :type: str
        """

        self._template_id = template_id

    @property
    def description(self):
        """Gets the description of this DocumentMeta.  # noqa: E501


        :return: The description of this DocumentMeta.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DocumentMeta.


        :param description: The description of this DocumentMeta.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def version(self):
        """Gets the version of this DocumentMeta.  # noqa: E501


        :return: The version of this DocumentMeta.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this DocumentMeta.


        :param version: The version of this DocumentMeta.  # noqa: E501
        :type: str
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def created_at(self):
        """Gets the created_at of this DocumentMeta.  # noqa: E501


        :return: The created_at of this DocumentMeta.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this DocumentMeta.


        :param created_at: The created_at of this DocumentMeta.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this DocumentMeta.  # noqa: E501


        :return: The updated_at of this DocumentMeta.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this DocumentMeta.


        :param updated_at: The updated_at of this DocumentMeta.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

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
        if not isinstance(other, DocumentMeta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
