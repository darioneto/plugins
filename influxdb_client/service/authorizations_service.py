# coding: utf-8

"""
    Influx API Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 0.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from influxdb_client.api_client import ApiClient


class AuthorizationsService(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_authorizations_id(self, auth_id, **kwargs):  # noqa: E501
        """Delete a authorization  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_authorizations_id(auth_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str auth_id: The ID of the authorization to delete. (required)
        :param str zap_trace_span: OpenTracing span context
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_authorizations_id_with_http_info(auth_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_authorizations_id_with_http_info(auth_id, **kwargs)  # noqa: E501
            return data

    def delete_authorizations_id_with_http_info(self, auth_id, **kwargs):  # noqa: E501
        """Delete a authorization  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_authorizations_id_with_http_info(auth_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str auth_id: The ID of the authorization to delete. (required)
        :param str zap_trace_span: OpenTracing span context
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['auth_id', 'zap_trace_span']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_authorizations_id" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'auth_id' is set
        if ('auth_id' not in local_var_params or
                local_var_params['auth_id'] is None):
            raise ValueError("Missing the required parameter `auth_id` when calling `delete_authorizations_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'auth_id' in local_var_params:
            path_params['authID'] = local_var_params['auth_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zap_trace_span' in local_var_params:
            header_params['Zap-Trace-Span'] = local_var_params['zap_trace_span']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/authorizations/{authID}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_authorizations(self, **kwargs):  # noqa: E501
        """List all authorizations  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_authorizations(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zap_trace_span: OpenTracing span context
        :param str user_id: Only show authorizations that belong to a user ID.
        :param str user: Only show authorizations that belong to a user name.
        :param str org_id: Only show authorizations that belong to an organization ID.
        :param str org: Only show authorizations that belong to a organization name.
        :return: Authorizations
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_authorizations_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_authorizations_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_authorizations_with_http_info(self, **kwargs):  # noqa: E501
        """List all authorizations  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_authorizations_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zap_trace_span: OpenTracing span context
        :param str user_id: Only show authorizations that belong to a user ID.
        :param str user: Only show authorizations that belong to a user name.
        :param str org_id: Only show authorizations that belong to an organization ID.
        :param str org: Only show authorizations that belong to a organization name.
        :return: Authorizations
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['zap_trace_span', 'user_id', 'user', 'org_id', 'org']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_authorizations" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_id' in local_var_params:
            query_params.append(('userID', local_var_params['user_id']))  # noqa: E501
        if 'user' in local_var_params:
            query_params.append(('user', local_var_params['user']))  # noqa: E501
        if 'org_id' in local_var_params:
            query_params.append(('orgID', local_var_params['org_id']))  # noqa: E501
        if 'org' in local_var_params:
            query_params.append(('org', local_var_params['org']))  # noqa: E501

        header_params = {}
        if 'zap_trace_span' in local_var_params:
            header_params['Zap-Trace-Span'] = local_var_params['zap_trace_span']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/authorizations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Authorizations',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_authorizations_id(self, auth_id, **kwargs):  # noqa: E501
        """Retrieve an authorization  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_authorizations_id(auth_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str auth_id: The ID of the authorization to get. (required)
        :param str zap_trace_span: OpenTracing span context
        :return: Authorization
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_authorizations_id_with_http_info(auth_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_authorizations_id_with_http_info(auth_id, **kwargs)  # noqa: E501
            return data

    def get_authorizations_id_with_http_info(self, auth_id, **kwargs):  # noqa: E501
        """Retrieve an authorization  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_authorizations_id_with_http_info(auth_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str auth_id: The ID of the authorization to get. (required)
        :param str zap_trace_span: OpenTracing span context
        :return: Authorization
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['auth_id', 'zap_trace_span']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_authorizations_id" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'auth_id' is set
        if ('auth_id' not in local_var_params or
                local_var_params['auth_id'] is None):
            raise ValueError("Missing the required parameter `auth_id` when calling `get_authorizations_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'auth_id' in local_var_params:
            path_params['authID'] = local_var_params['auth_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zap_trace_span' in local_var_params:
            header_params['Zap-Trace-Span'] = local_var_params['zap_trace_span']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/authorizations/{authID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Authorization',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def patch_authorizations_id(self, auth_id, authorization_update_request, **kwargs):  # noqa: E501
        """Update an authorization to be active or inactive  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_authorizations_id(auth_id, authorization_update_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str auth_id: The ID of the authorization to update. (required)
        :param AuthorizationUpdateRequest authorization_update_request: Authorization to update (required)
        :param str zap_trace_span: OpenTracing span context
        :return: Authorization
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.patch_authorizations_id_with_http_info(auth_id, authorization_update_request, **kwargs)  # noqa: E501
        else:
            (data) = self.patch_authorizations_id_with_http_info(auth_id, authorization_update_request, **kwargs)  # noqa: E501
            return data

    def patch_authorizations_id_with_http_info(self, auth_id, authorization_update_request, **kwargs):  # noqa: E501
        """Update an authorization to be active or inactive  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_authorizations_id_with_http_info(auth_id, authorization_update_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str auth_id: The ID of the authorization to update. (required)
        :param AuthorizationUpdateRequest authorization_update_request: Authorization to update (required)
        :param str zap_trace_span: OpenTracing span context
        :return: Authorization
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['auth_id', 'authorization_update_request', 'zap_trace_span']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_authorizations_id" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'auth_id' is set
        if ('auth_id' not in local_var_params or
                local_var_params['auth_id'] is None):
            raise ValueError("Missing the required parameter `auth_id` when calling `patch_authorizations_id`")  # noqa: E501
        # verify the required parameter 'authorization_update_request' is set
        if ('authorization_update_request' not in local_var_params or
                local_var_params['authorization_update_request'] is None):
            raise ValueError("Missing the required parameter `authorization_update_request` when calling `patch_authorizations_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'auth_id' in local_var_params:
            path_params['authID'] = local_var_params['auth_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zap_trace_span' in local_var_params:
            header_params['Zap-Trace-Span'] = local_var_params['zap_trace_span']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'authorization_update_request' in local_var_params:
            body_params = local_var_params['authorization_update_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/authorizations/{authID}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Authorization',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_authorizations(self, authorization, **kwargs):  # noqa: E501
        """Create an authorization  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_authorizations(authorization, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Authorization authorization: Authorization to create (required)
        :param str zap_trace_span: OpenTracing span context
        :return: Authorization
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_authorizations_with_http_info(authorization, **kwargs)  # noqa: E501
        else:
            (data) = self.post_authorizations_with_http_info(authorization, **kwargs)  # noqa: E501
            return data

    def post_authorizations_with_http_info(self, authorization, **kwargs):  # noqa: E501
        """Create an authorization  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_authorizations_with_http_info(authorization, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Authorization authorization: Authorization to create (required)
        :param str zap_trace_span: OpenTracing span context
        :return: Authorization
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['authorization', 'zap_trace_span']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_authorizations" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in local_var_params or
                local_var_params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `post_authorizations`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'zap_trace_span' in local_var_params:
            header_params['Zap-Trace-Span'] = local_var_params['zap_trace_span']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'authorization' in local_var_params:
            body_params = local_var_params['authorization']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/authorizations', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Authorization',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
